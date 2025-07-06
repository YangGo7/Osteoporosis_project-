from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from user.models import Profile 

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Profile.objects.create(user=user)  # 회원가입 시 프로필 자동 생성
        return user
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['age', 'gender', 'height','weight', 'fracture', 'smoking', 'calcitriol', 
            'op', 'ckd', 'copd', 'dm', 'drinking']
        widgets = {
            'gender': forms.Select(choices=[('Male', 'Male'), ('Female', 'Female')]),  # 성별 선택
        }
