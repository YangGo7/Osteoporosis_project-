from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import TemplateView
from user.forms import NewUserForm
from django.contrib import messages
from user.forms import ProfileForm  # ✅ 올바른 경로

# render를 사용하지 않고, class base로 서비스할 때 사용하는 게 TemplateView이다.
class HomeView(TemplateView):
    template_name = 'osteoporosis' 
    def get_context_data(self, **kwargs):  # 오버라이딩
        context = super(HomeView, self).get_context_data(**kwargs)
        return context
