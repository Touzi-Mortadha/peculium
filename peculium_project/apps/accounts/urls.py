from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views
from .views import IndexView, LoginUserView, UpdateUserView, LogoutUserView, account_activation_sent, \
    activate, signup, UpdateAdminView, ConfiTCLViewSet

pcl_list = views.ConfiTCLViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
pcl_detail = views.ConfiTCLViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    # HOME Page
    url(r'^$', IndexView.as_view(), name='index_view'),
    # LOGIN/LOGOUT
    url(r'^login/', LoginUserView.as_view(), name='login'),
    url(r'^logout/', LogoutUserView.as_view(), name='logout'),
    # PROFILES
    url(r'^user/profile/', UpdateUserView.as_view(), name='profile'),
    url(r'^user/admin/$', UpdateAdminView.as_view(), name='admin'),
    # SIGN UP
    url(r'signup/$', signup.as_view(), name='signup'),
    # account activation sent
    url(r'account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    # activate with token
    url(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    # RESET PASSWORD
    url(r'^', include('django.contrib.auth.urls')),
    # API urls
    url(r'^api/pcls/$', pcl_list, name='pcl_list'),
    url(r'^api/pcl/(?P<pk>\d+)/$', pcl_detail, name='pcl_detail'),

]
