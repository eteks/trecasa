from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView


# Create your views here.
class Index_pageview(TemplateView):
    template_name = "index.html"
class Actividades_pageview(TemplateView):
    template_name = "actividades.html"
class Register_pageview(TemplateView):
	template_name = "register.html"
class Gymbcn_pageview(TemplateView):
	template_name = "gymbcn.html"