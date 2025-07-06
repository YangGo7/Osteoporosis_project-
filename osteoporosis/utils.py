from django.shortcuts import render
import numpy as np
import os
from django.conf import settings
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa
import datetime

import math

# 수식 기반 로직 사용
def logistic_function(x):
    return 1 / (1 + math.exp(-x))

def predict_osteoporosis(data):
    age = data['age']
    gender = data['gender']
    bmi = data['weight'] / ((data['height'] / 100) ** 2)

    fracture = data['fracture']
    smoking = data['smoking']
    drinking = data['drinking']
    calcitriol = data['calcitriol']
    op = data['op']
    ckd = data['ckd']
    copd = data['copd']
    dm = data['dm']

    bmi_score = -0.1 * (bmi - 25)

    coef = {
        'intercept': -4.0,
        'age': 0.05 * age,
        'gender': -0.3 if gender == '여자' else 0,
        'bmi': bmi_score,
        'fracture': 0.8 if fracture else 0,
        'smoking': 0.5 if smoking else 0,
        'calcitriol': 0.4 if calcitriol else 0,
        'op': 0.6 if op else 0,
        'ckd': 0.3 if ckd else 0,
        'copd': 0.3 if copd else 0,
        'dm': 0.3 if dm else 0,
        'drinking': 0.3 if drinking else 0,
    }

    logit_major = sum(coef.values())
    logit_hip = logit_major - 1.5
    logit_op = logit_major - 1.0

    major_risk = round(logistic_function(logit_major) * 100, 2)
    hip_risk = round(logistic_function(logit_hip) * 100, 2)
    osteoporosis = round(logistic_function(logit_op) * 100, 2)

    # 위험도 라벨: 낮음(0), 중간(1), 높음(2)
    if osteoporosis >= 20:
        level_label = 2
    elif osteoporosis >= 10:
        level_label = 1
    else:
        level_label = 0

    return {
        'major_risk': major_risk,
        'hip_risk': hip_risk,
        'level': ['낮음', '중간', '높음'][level_label]
    }
    
def pdf_view(request):
    name = request.GET.get('name', 'Unknown')
    major_risk = request.GET.get('major_risk', '0')
    hip_risk = request.GET.get('hip_risk', '0')
    osteoporosis_risk = request.GET.get('osteoporosis_risk', '0')
    risk_level = request.GET.get('risk_level', 'Normal')
   

    context = {
        'major_risk': major_risk,
        'hip_risk': hip_risk,
        'osteoporosis_risk': osteoporosis_risk,
        'risk_level': risk_level,
    }

    template = get_template('prediction/pdf_template.html')
    html = template.render(context) 

    response = HttpResponse(content_type='application/pdf')
    pisa_status = pisa.CreatePDF(html, dest=response, encoding='utf-8')

    if pisa_status.err:
        return HttpResponse('PDF creation error occurred.')
    return response
