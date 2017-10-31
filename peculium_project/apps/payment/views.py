from django.shortcuts import render
from django.views.generic import TemplateView
from .serializers import GetCurrencySerializer
from .models import GetCurrency
from rest_framework import viewsets

class PayementView(TemplateView):
    template_name = "payement.html"


class GetCurrencyViewSet(viewsets.ModelViewSet):
    queryset = GetCurrency.objects.all()
    serializer_class = GetCurrencySerializer


