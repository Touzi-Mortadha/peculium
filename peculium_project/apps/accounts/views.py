from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

class IndexView(TemplateView):
    template_name = "home.html"


class LoginUserView(auth_views.LoginView):
    template_name = "Login/login.html"
    redirect_field_name = reverse_lazy("profile")


class LogoutUserView(auth_views.LogoutView):
    redirect_field_name = reverse_lazy("login")


@method_decorator(login_required, name='dispatch')
class UpdateUserView(TemplateView):
    template_name = "profile.html"


