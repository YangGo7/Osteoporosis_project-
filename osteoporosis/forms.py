# forms.py
from django import forms
from .models import Osteoporosis

class OsteoporosisForm(forms.ModelForm):
    class Meta:
        model = Osteoporosis
        fields = '__all__'
        widgets = {
            'fracture': forms.RadioSelect(choices=[(True, '예'), (False, '아니오')]),
            'smoking': forms.RadioSelect(choices=[(True, '예'), (False, '아니오')]),
            'drinking': forms.RadioSelect(choices=[(True, '예'), (False, '아니오')]),
            'calcitriol': forms.RadioSelect(choices=[(True, '예'), (False, '아니오')]),
            'op': forms.RadioSelect(choices=[(True, '예'), (False, '아니오')]),
            'ckd': forms.RadioSelect(choices=[(True, '예'), (False, '아니오')]),
            'copd': forms.RadioSelect(choices=[(True, '예'), (False, '아니오')]),
            'dm': forms.RadioSelect(choices=[(True, '예'), (False, '아니오')]),
        }
