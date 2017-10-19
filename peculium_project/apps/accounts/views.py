from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import SignUpForm
from django.contrib.auth import login

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.views import View
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage


class IndexView(TemplateView):
    template_name = "home.html"


class LoginUserView(auth_views.LoginView):
    template_name = "Login/login.html"
    redirect_field_name = reverse_lazy("profile")


class LogoutUserView(auth_views.LogoutView):
    redirect_field_name = reverse_lazy("login")


class signup(View):
    form_class = SignUpForm
    template_name = 'Login/signup.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your Soteq Account'
            message = render_to_string('activation_email/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            toemail = form.cleaned_data.get('email')
            email = EmailMessage(subject, message, to=[toemail])
            email.send()
            return redirect('account_activation_sent')
        return render(request, self.template_name, {'form': form})

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})


@method_decorator(login_required, name='dispatch')
class UpdateUserView(TemplateView):
    template_name = "profile.html"


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.userprofile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('index_view')
    else:
        return render(request, 'activation_email/account_activation_invalid.html')


def account_activation_sent(request):
    return render(request, 'activation_email/account_activation_sent.html')
