from django.urls import path
from .views import register_request, login_request, logout_request
from .views import mypage_edit , mypage
app_name = 'user'
urlpatterns = [
    path('register/', register_request, name='register'),
    path('login/', login_request, name='login'),
    path('logout/', logout_request, name='logout'),
    path("mypage/", mypage, name="mypage"),
    path('mypage_edit/', mypage_edit, name='mypage_edit'),
]
