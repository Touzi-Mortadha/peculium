from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

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



