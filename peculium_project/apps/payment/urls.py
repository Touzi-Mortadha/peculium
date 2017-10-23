from django.conf.urls import url, include
from .views import PayementView

urlpatterns = [
    url(r'^', PayementView.as_view(), name='payement'),

]
