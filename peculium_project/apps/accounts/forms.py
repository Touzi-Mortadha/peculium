from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    public_rib=forms.CharField(max_length=254, help_text='Required. Enter a valid public key .', required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'public_rib', 'password1', 'password2',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'A user with that email already exists.')
        return email

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control input-lg'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control input-lg'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control input-lg'})
        self.fields['email'].widget.attrs.update({'class': 'form-control input-lg'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control input-lg'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control input-lg'})

# class SignUpProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ('adresse',)
#     def __init__(self, *args, **kwargs):
#         super(SignUpProfileForm, self).__init__(*args, **kwargs)
#         self.fields['adresse'].widget.attrs.update({'class': 'form-control input-lg'})




class PublicRibForm(forms.ModelForm):
    public_rib=forms.CharField(max_length=254, help_text='Required. Enter a valid public rib .', required=False)

    class Meta:
        model = User
        fields = ('public_rib',)

    def __init__(self, *args, **kwargs):
        super(PublicRibForm, self).__init__(*args, **kwargs)
        self.fields['public_rib'].widget.attrs.update({'class': 'form-control input-lg'})



class AdminRibsForm(forms.ModelForm):
    banc_rib=forms.CharField(max_length=254, help_text='Required. Enter a valid banc rib .', required=False)
    BTC_rib=forms.CharField(max_length=254, help_text='Required. Enter a valid BTC rib .', required=False)
    ETH_rib=forms.CharField(max_length=254, help_text='Required. Enter a valid ETH rib .', required=False)

    class Meta:
        model = User
        fields = ('banc_rib', 'BTC_rib', 'ETH_rib',)

    def __init__(self, *args, **kwargs):
        super(AdminRibsForm, self).__init__(*args, **kwargs)
        self.fields['banc_rib'].widget.attrs.update({'class': 'form-control input-lg'})
        self.fields['BTC_rib'].widget.attrs.update({'class': 'form-control input-lg'})
        self.fields['ETH_rib'].widget.attrs.update({'class': 'form-control input-lg'})