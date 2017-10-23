from django.conf.urls import url, include

from django.contrib.auth import views as auth_views
from . import views
from .views import IndexView, LoginUserView, UpdateUserView, LogoutUserView, PayementView, account_activation_sent, \
    activate, signup, UpdateAdminView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index_view'),
    # url(r'^home/', IndexView.as_view(), name='index_view'),
    url(r'^user/login/', LoginUserView.as_view(), name='login'),
    url(r'^user/logout/', LogoutUserView.as_view(), name='logout'),
    url(r'^user/profile/', UpdateUserView.as_view(), name='profile'),
    url(r'^user/payement/', PayementView.as_view(), name='payement'),
    url(r'^user/admin/$', UpdateAdminView.as_view(), name='admin'),
    # sign up
    url(r'signup/$', signup.as_view(), name='signup'),
    # url(r'rest_password/$', ResetPassword.as_view(), name='rest_password'),
    # account activation sent
    url(r'account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    # activate with token
    url(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    # url(r'^user/', include('django.contrib.auth.urls')),

    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),

]
