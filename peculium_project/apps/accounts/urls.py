from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from .views import IndexView, LoginUserView, UpdateUserView, LogoutUserView, account_activation_sent, \
    activate, signup, UpdateAdminView, ConfiTCLViewSet, UserProfileViewSet, AddPublicRibView, UpdateRibsView

pcl_list = ConfiTCLViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
pcl_detail = ConfiTCLViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

user_detail = UserProfileViewSet.as_view({
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

    # SET PUBLIC RIB
url(r'^user/public_rib/', AddPublicRibView.as_view(), name='public-rib'),


 # MODIFY ADMIN RIBS
url(r'^user/admin/ribs', UpdateRibsView.as_view(), name='modify-ribs'),

    # SIGN UP
    url(r'signup/$', signup.as_view(), name='signup'),
    # account activation sent
    url(r'account_activation_sent/$', account_activation_sent, name='account_activation_sent'),
    # activate with token
    url(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
    # RESET PASSWORD
    url(r'^', include('django.contrib.auth.urls')),
    # API urls
    url(r'^api/pcls/$', pcl_list, name='pcl_list'),
    url(r'^api/pcl/(?P<pk>\d+)/$', pcl_detail, name='pcl_detail'),
    url(r'^api/user/(?P<pk>\d+)/$', user_detail, name='user_detail'),
]
