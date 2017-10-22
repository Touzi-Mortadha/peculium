from django.conf.urls import url
from . import views
from .views import IndexView, LoginUserView, UpdateUserView, LogoutUserView, account_activation_sent, activate, signup, UpdateAdminView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index_view'),
    # url(r'^home/', IndexView.as_view(), name='index_view'),
    url(r'^user/login/', LoginUserView.as_view(), name='login'),
    url(r'^user/logout/', LogoutUserView.as_view(), name='logout'),
    url(r'^user/profile/', UpdateUserView.as_view(), name='profile'),
    url(r'^user/admin/', UpdateAdminView.as_view(), name='admin'),
    # sign up
    url(r'signup/$', signup.as_view(), name='signup'),
    # url(r'rest_password/$', ResetPassword.as_view(), name='rest_password'),
    # account activation sent
    url(r'account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    # activate with token
    url(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]
