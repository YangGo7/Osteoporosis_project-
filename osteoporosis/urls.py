from django.urls import path
from . import views
from .pdf_views import pdf_view
app_name = 'osteoporosis'

urlpatterns = [
    path('', views.osteoporosis_input, name='osteoporosis_input'),
    path('results/', views.osteoporosis_result_list, name='result_list'),
    path('pdf/', views.pdf_view, name='pdf_my'),
    path('result/<int:result_id>/', views.result_detail, name='result_detail'),
    path('osteoporosis/qrcode/<int:result_id>/', views.qr_code_view, name='osteoporosis_qrcode'),
]