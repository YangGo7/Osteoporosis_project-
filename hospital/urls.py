from django.urls import path
from . import views

app_name = 'hospital'

urlpatterns = [
    path('', views.hospital_list, name='hospital'),
    path('get-districts/', views.get_districts, name='get_districts'),
]
