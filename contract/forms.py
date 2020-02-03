from django import forms
from .models import ContractModels

class ContractForms(forms.ModelForm):
    
    class Meta:
        model = ContractModels
        fields = '__all__'