from django.conf.urls import url, include
from .views import PayementView, GetCurrencyViewSet




currency_list = GetCurrencyViewSet.as_view({
    'get': 'list',
})

urlpatterns = [
    url(r'^$', PayementView.as_view(), name='payement'),
url(r'^api/currency/$', currency_list, name='currency_list'),

]
