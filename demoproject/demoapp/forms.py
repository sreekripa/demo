from . models import shops
from django import forms

class ModeForm(forms.ModelForm):
    class Meta:
        model=shops
        fields=['name','desc','img','price']
