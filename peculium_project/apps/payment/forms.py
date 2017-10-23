from django import forms
from .models import ConfiTCL



class ConfigPCLForm(forms.ModelForm):
    """This class represents the Config Email form"""
    class Meta:
        model = ConfiTCL
        fields = ('number_of_PCL', 'PCL_amount',)
        widgets = {
            'number_of_PCL': forms.TextInput(attrs={'class': 'form-control'}),
            'PCL_amount': forms.TextInput(attrs={'class': 'form-control'}),
        }