from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import NewUserForm, ProfileForm

# ✅ 회원가입
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = NewUserForm()
    
    return render(request, "user/register.html", {"register_form": form})

# ✅ 로그인
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()

    return render(request, "user/login.html", {"form": form})

# ✅ 로그아웃
def logout_request(request):
    logout(request)
    return redirect("home")

# ✅ 마이페이지 조회 (유저 정보 출력)
@login_required
def mypage(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, "user/mypage.html", {"profile": profile})

# ✅ 마이페이지 수정 (정보 수정 가능)
@login_required
def mypage_edit(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("user:mypage")  # 수정 후 마이페이지로 이동
    else:
        form = ProfileForm(instance=profile)

    return render(request, "user/mypage_edit.html", {"form": form})
