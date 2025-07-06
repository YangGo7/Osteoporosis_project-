"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from mysite import views
from osteoporosis.views import osteoporosis_input
# 여기 주소는 http://127.0.0.1:8000 지정되어 있다. (뒤로 /polls나 /admin을 쓴 것). 아무것도 없을 땐 views가 나오는 것.
urlpatterns = [
    path("admin/", admin.site.urls),
    # polls로 가게 하기 위한 코드  # 앱.. 여는 거 할 때 include 포함함
    path('', osteoporosis_input, name='home'),   # class인 경우에 as_view를 붙여준다.
    path('user/', include('user.urls')),  # 유저 관련 기능
    path('post/', include('post.urls')),
     path("hospital/", include("hospital.urls")),
    path('osteoporosis/', include('osteoporosis.urls')),
    ]
