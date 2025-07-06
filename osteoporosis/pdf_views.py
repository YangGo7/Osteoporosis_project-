from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from osteoporosis.models import OsteoporosisResult
import os
from django.conf import settings

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = HttpResponse(content_type='application/pdf')
    pisa_status = pisa.CreatePDF(html, dest=result)
    if pisa_status.err:
        return HttpResponse('PDF 생성 실패: %s' % pisa_status.err)
    return result

from django.shortcuts import get_object_or_404

def pdf_view(request):
    name = request.GET.get('name', '')
    major_risk = request.GET.get('major_risk')
    hip_risk = request.GET.get('hip_risk')
    risk_level = request.GET.get('risk_level')

    # 모든 값이 있어야 조회 가능
    if not (name and major_risk and hip_risk and risk_level):
        return HttpResponse("필수 예측값이 누락되었습니다.", status=400)

    try:
        major_risk = float(major_risk)
        hip_risk = float(hip_risk)
    except ValueError:
        return HttpResponse("예측값은 숫자여야 합니다.", status=400)

    # DB에서 저장된 결과 가져오기
    result = OsteoporosisResult.objects.filter(
        name=name,
        major_risk=major_risk,
        hip_risk=hip_risk,
        level=risk_level
    ).last()

    if not result:
        return HttpResponse("일치하는 예측 결과를 찾을 수 없습니다.", status=404)

    context = {
        'name': result.name,
        'major_risk': result.major_risk,
        'hip_risk': result.hip_risk,
        'osteoporosis_risk': result.osteoporosis_risk,
        'risk_level': result.level,
        'result_id': result.id,
    }

    return render_to_pdf('prediction/pdf_template.html', context)
