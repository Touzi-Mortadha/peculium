from django.conf.urls import url

from .views import IndexView, LoginUserView, UpdateUserView, LogoutUserView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^user/login/$', LoginUserView.as_view(), name='login'),
    url(r'^user/logout/$', LogoutUserView.as_view(), name='logout'),
    url(r'^user/profile/$', UpdateUserView.as_view(), name='profile'),
]
