from django.shortcuts import render
from django.views import generic
# Create your views here.
class testView(generic.TemplateView):
    template_name = "pqrs/index.html"