from .models import Database
from django import forms

class MyForm(forms.ModelForm):
    class Meta:
        model= Database
        fields='__all__'