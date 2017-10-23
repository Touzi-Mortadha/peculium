from django.shortcuts import render
from django.views.generic import TemplateView

class PayementView(TemplateView):
    template_name = "payement.html"


