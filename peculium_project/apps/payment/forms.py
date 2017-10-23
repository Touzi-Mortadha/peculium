from django import forms
from .models import ConfiTCL



class ConfigPCLForm(forms.ModelForm):
    """This class represents the Config Email form"""
    class Meta:
        model = ConfiTCL
        fields = ('number_of_tokens', 'amount',)
        widgets = {
            'number_of_tokens': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
        }