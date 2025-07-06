from django import forms
from .models import Post, Reply

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'is_secret']  # is_secret 필드 추가

    is_secret = forms.BooleanField(required=False, label="비밀글로 작성", initial=False)  # 비밀글 체크박스

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content', 'is_secret']  # 댓글 내용과 비밀글 여부 추가
        labels = {
            'is_secret': '비밀'  # 체크박스 라벨 변경
        }
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': '답변을 입력하세요'}),
            'is_secret': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }