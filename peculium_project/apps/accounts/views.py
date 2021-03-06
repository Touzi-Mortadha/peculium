from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
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
from django.utils.html import strip_tags
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.template.response import TemplateResponse
from ..payment.models import ConfiTCL
from rest_framework import viewsets
from ..payment.serializers import ConfiTCLSerializer
from .serializers import UserProfileSerializer
from .models import UserProfile, Transaction
from .forms import SignUpForm, PublicRibForm, AdminRibsForm
from ..payment.forms import ConfigPCLForm, ConfigUsedTCLForm
import datetime
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail


class IndexView(TemplateView):
    template_name = "home.html"


class LoginUserView(auth_views.LoginView):
    template_name = "Login/login.html"

    def get_success_url(self):
        url = self.get_redirect_url()
        if url:
            return url
        elif self.request.user.is_superuser:
            return reverse("admin")
        else:
            return reverse("profile")


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
            if form.data['public_rib']:
                user.userprofile.public_rib = form.cleaned_data.get('public_rib')
                user.userprofile.save()
            current_site = get_current_site(request)
            subject = 'Activate Your Peculium Account'
            toemail = form.cleaned_data.get('email')
            msg_plain = render_to_string('activation_email/content.txt', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            message = render_to_string('activation_email/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            send_mail(
                subject,
                msg_plain,
                'peculium',
                [toemail],
                html_message=message,
            )

            return redirect('account_activation_sent')
        return render(request, self.template_name, {'form': form})

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})


class UpdateUserView(TemplateView):
    template_name = "profile.html"

    @method_decorator(user_passes_test(lambda u: not u.is_superuser))
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        userr = User.objects.get(username='peculium')
        inst = ConfiTCL.objects.get(user=userr)
        tmp = inst.TCL_USED
        form = ConfigUsedTCLForm(request.POST, instance=inst)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.TCL_USED = tmp + form.cleaned_data['TCL_USED']
            activ = self.request.user.userprofile
            activ.buy = True
            activ.save()
            obj.save()
            transaction = Transaction()
            transaction.user = request.user.userprofile
            transaction.date_of_transaction = datetime.datetime.now().date()
            transaction.time_of_transaction = datetime.datetime.now().time()
            transaction.TCL_assigned = form.cleaned_data['TCL_USED']
            transaction.save()

            return redirect('profile')
        user_buy = UserProfile.objects.all().count()
        context = {'amount': inst.PCL_amount,
                   'number_of_tokens': inst.number_of_PCL,
                   'user': self.request.user,
                   'user_buy': user_buy,
                   'form': form,
                   'banc_rib': str(userr.userprofile.banc_rib),
                   'BTC_rib': str(userr.userprofile.BTC_rib),
                   'ETH_rib': str(userr.userprofile.ETH_rib)}
        return render(request, self.template_name, context)

    def get(self, request, *args, **kwargs):
        userr = User.objects.get(username='peculium')
        inst = ConfiTCL.objects.get(user=userr)
        form = ConfigUsedTCLForm(instance=inst)
        user_buy = UserProfile.objects.filter(buy=True).count()
        context = {'amount': inst.PCL_amount,
                   'all_amount': inst.PCL_amount * inst.number_of_PCL,
                   'number_of_tokens': inst.number_of_PCL,
                   'TCL_USED': inst.TCL_USED,
                   'user': self.request.user,
                   'user_buy': user_buy,
                   'form': form,
                   'banc_rib': str(userr.userprofile.banc_rib),
                   'BTC_rib': str(userr.userprofile.BTC_rib),
                   'ETH_rib': str(userr.userprofile.ETH_rib)}

        return TemplateResponse(request, self.template_name, context)

        # def get_context_data(self, **kwargs):
        #     context = super(UpdateUserView, self).get_context_data(**kwargs)
        #     context['user'] = self.request.user
        #     return context


class UpdateAdminView(TemplateView):
    template_name = "admin.html"

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        userr = User.objects.get(username=request.user)
        inst = ConfiTCL.objects.get(user=userr)
        form = ConfigPCLForm(request.POST, instance=inst)
        if form.is_valid():
            form.save()
        return TemplateResponse(request, self.template_name,
                                {'form': form,
                                 'user': self.request.user,
                                 'amount': inst.PCL_amount,
                                 'number_of_tokens': inst.number_of_PCL,
                                 'banc_rib': request.user.userprofile.banc_rib,
                                 'BTC_rib': request.user.userprofile.BTC_rib,
                                 'ETH_rib': request.user.userprofile.ETH_rib
                                 })

    def get(self, request, *args, **kwargs):
        userr = User.objects.get(username=request.user)
        inst = ConfiTCL.objects.get(user=userr)
        form = ConfigPCLForm(instance=inst)
        context = {'form': form, 'user': self.request.user,
                   'amount': inst.PCL_amount,
                   'number_of_tokens': inst.number_of_PCL,
                   'banc_rib': request.user.userprofile.banc_rib,
                   'BTC_rib': request.user.userprofile.BTC_rib,
                   'ETH_rib': request.user.userprofile.ETH_rib
                   }
        return TemplateResponse(request, self.template_name, context)

        # def get_context_data(self, **kwargs):
        #     context = super(UpdateAdminView, self).get_context_data(**kwargs)
        #     context['user'] = self.request.user
        #     return context


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
        return redirect('profile')
    else:
        return render(request, 'activation_email/account_activation_invalid.html')


def account_activation_sent(request):
    return render(request, 'activation_email/account_activation_sent.html')


class AddPublicRibView(TemplateView):
    template_name = "public_rib.html"

    @method_decorator(user_passes_test(lambda u: not u.is_superuser))
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = PublicRibForm(request.POST, instance=request.user)
        if form.is_valid():
            request.user.userprofile.public_rib = form.cleaned_data['public_rib']
            request.user.userprofile.save()
            return redirect('profile')
        context = {'user': self.request.user,
                   'form': form,
                   }
        return render(request, self.template_name, context)

    def get(self, request, *args, **kwargs):
        form = PublicRibForm(instance=request.user)
        context = {'user': self.request.user,
                   'form': form,
                   }

        return TemplateResponse(request, self.template_name, context)


class UpdateRibsView(TemplateView):
    template_name = "modify_ribs.html"

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        form = AdminRibsForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            request.user.userprofile.BTC_rib = form.cleaned_data['BTC_rib']
            request.user.userprofile.ETH_rib = form.cleaned_data['ETH_rib']
            request.user.userprofile.banc_rib = form.cleaned_data['banc_rib']
            request.user.userprofile.save()

        return TemplateResponse(request, self.template_name, {'form': form,
                                                              'user': request.user
                                                              })

    def get(self, request, *args, **kwargs):
        form = AdminRibsForm(instance=request.user.userprofile)
        context = {'form': form,
                   'user': request.user
                   }
        return TemplateResponse(request, self.template_name, context)


# API VIEWSETS

class ConfiTCLViewSet(viewsets.ModelViewSet):
    queryset = ConfiTCL.objects.all()
    serializer_class = ConfiTCLSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
