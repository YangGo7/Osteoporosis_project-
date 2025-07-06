from django.shortcuts import render, redirect ,get_object_or_404
from .forms import OsteoporosisForm
from .utils import predict_osteoporosis  # 사용 시 필요
from .models import OsteoporosisResult
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import numpy as np
import qrcode
import io
import base64
from django.shortcuts import render
from .forms import OsteoporosisForm
from .utils import predict_osteoporosis  # 여전히 쓰는 경우
from .models import OsteoporosisResult
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import numpy as np
import random
# ➤ 로지스틱 함수
def logistic_function(x):
    return 1 / (1 + np.exp(-x))

# ➤ 위험도 계산 함수
def calculate_frax_risk(age, gender, bmi, fracture, smoking, calcitriol, op, ckd, copd, dm, drinking):
    bmi_score = -0.1 * (bmi - 25)
    coef = {
        "intercept": -4.0,
        "age": 0.05 * age,
        "gender": 0.3 if gender == 1 else 0,
        "bmi": bmi_score,
        "fracture": 0.8 if fracture else 0,
        "smoking": 0.5 if smoking else 0,
        "calcitriol": 0.4 if calcitriol else 0,
        "OP": 0.6 if op else 0,
        "ckd": 0.3 if ckd else 0,
        "copd": 0.3 if copd else 0,
        "dm": 0.3 if dm else 0,
        "drinking": 0.3 if drinking else 0,
    }
    logit_major = sum(coef.values())
    logit_hip = logit_major - 1.5
    logit_osteo = logit_major - 1.0

    return (
        round(logistic_function(logit_major) * 100, 2),
        round(logistic_function(logit_hip) * 100, 2),
        round(logistic_function(logit_osteo) * 100, 2)
    )

# ➤ BMI 계산 함수
def get_bmi(height, weight):
    return weight / ((height / 100) ** 2)

# ➤ 위험 수준 분류
def classify_risk(score):
    if score >= 5:
        return "High Risk"
    elif score >= 3:
        return "Caution"
    else:
        return "Normal"

# ➤ 메인 입력 및 결과 처리 뷰

def osteoporosis_input(request):
    result = None
    user_info = None
    exercises = []  # GET 요청 대비 초기화
    foods = {}      # GET 요청 대비 초기화

    if request.method == 'POST':
        form = OsteoporosisForm(request.POST)
        if form.is_valid():
            user_info = form.save()

            bmi = get_bmi(user_info.height, user_info.weight)

            major_risk, hip_risk, osteoporosis_risk = calculate_frax_risk(
                user_info.age, user_info.gender, bmi,
                user_info.fracture, user_info.smoking, user_info.calcitriol,
                user_info.op, user_info.ckd, user_info.copd, user_info.dm, user_info.drinking
            )

            risk_level = classify_risk(osteoporosis_risk)
            exercises, foods = get_recommendations(risk_level)

            result_obj = OsteoporosisResult.objects.create(
                user=request.user,
                name=user_info.name,
                major_risk=major_risk,
                hip_risk=hip_risk,
                level=risk_level,
            )

            result = {
                'major_risk': major_risk,
                'hip_risk': hip_risk,
                'osteoporosis_risk': osteoporosis_risk,
                'level': risk_level,
                'result_id': result_obj.id,
                'name': user_info.name,
            }
    else:
        form = OsteoporosisForm()

    return render(request, 'osteoporosis/input.html', {
        'form': form,
        'result': result,
        'user': user_info,
        'exercises': exercises,
        'foods': foods,
    })


# ➤ PDF 출력 뷰

def pdf_view(request):
    name = request.GET.get('name', '')
    major_risk = request.GET.get('major_risk', '')
    hip_risk = request.GET.get('hip_risk', '')
    osteoporosis_risk = request.GET.get('osteoporosis_risk', '')
    risk_level = request.GET.get('risk_level', '')

    try:
        result = OsteoporosisResult.objects.filter(
            name=name,
            major_risk=major_risk,
            hip_risk=hip_risk,
            level=risk_level
        ).last()
    except ValueError:
        result = None

    qr_image_base64 = None
    if result:
        ngrok_url = " https://8256-121-183-211-161.ngrok-free.app"
        url = f"{ngrok_url}/osteoporosis/result/{result.id}/"
        img = qrcode.make(url)
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        qr_image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    context = {
        'name': name,
        'major_risk': major_risk,
        'hip_risk': hip_risk,
        'osteoporosis_risk': osteoporosis_risk,
        'risk_level': risk_level,
        'qr_image_base64': qr_image_base64,
    }

    template = get_template('osteoporosis/pdf_template.html')
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{name}_osteoporosis_report.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response, encoding='utf-8')

    if pisa_status.err:
        return HttpResponse('PDF 생성 중 오류 발생!')
    return response

# ➤ 결과 리스트

def osteoporosis_result_list(request):
    results = OsteoporosisResult.objects.filter(user=request.user).order_by('-id')
    return render(request, 'osteoporosis/result_list.html', {'results': results})

# ➤ QR 코드 이미지 반환

def qr_code_view(request, result_id):
    local_ip = "192.168.0.101"  # 현재 PC의 로컬 IP 주소로 교체
    port = 8000
    # 예: views.py 안에서
    ngrok_url = " https://8256-121-183-211-161.ngrok-free.app"
    url = f"{ngrok_url}/osteoporosis/result/{result_id}/"
    img = qrcode.make(url)

    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return HttpResponse(buffer.getvalue(), content_type="image/png")



@login_required
def result_detail(request, result_id):
    result = get_object_or_404(OsteoporosisResult, id=result_id, user=request.user)

    context = {
        'result': result,
    }
    return render(request, 'osteoporosis/result_detail.html', context)

LOW_RISK_EXERCISES = ['러닝', '요가', '고강도 웨이트']
MEDIUM_RISK_EXERCISES = ['필라테스', '계단 오르기', '중강도 웨이트']
HIGH_RISK_EXERCISES = ['가벼운 에어로빅', '의자잡고 뒤꿈치 들기', '가볍게 걷기']

FOODS= [{'image' : 'img/lunch1.png',
         'items' :['산채비빔밥밥', '고등어구이','배추김치','두부부침', '소고기무국']},
        {'image' : 'img/lunch3.png',
         'items' :['그릭요거트','견과류', '사과', '삶음계란', '두유']},
        {'image' : 'img/lunch2.png',
         'items' :['콩밥', '수육', '고추', '찐양배추', '버섯전골']}]

def get_recommendations(risk_level):
    if risk_level == "Normal":
        exercises = random.sample(LOW_RISK_EXERCISES, 3)
    elif risk_level == "Caution":
        exercises = random.sample(MEDIUM_RISK_EXERCISES, 3)
    else:
        exercises = random.sample(HIGH_RISK_EXERCISES, 3)
        
    foods = random.choice(FOODS)
    return exercises, foods