from django.shortcuts import render
from django.views.generic.base import TemplateView


class MainPage(TemplateView):
    template_name = 'static_page/index.html'
