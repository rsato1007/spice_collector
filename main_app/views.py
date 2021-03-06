from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView

from .models import Spices

# Create your views here.

# This is what actual serves the home page template
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class Index(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["spices"] = Spices.objects.all() # Here we are using the model to query the database for us
        return context

class SpicesCreate(CreateView):
    model = Spices
    fields = ['name', 'description', 'cuisine', 'shelf_life']
    template_name = "spices_create.html"
    success_url = "/index/"

class SpicesDetail(DetailView):
    model = Spices
    template_name = "spice_detail.html"

class SpicesUpdate(UpdateView):
    model = Spices
    fields = ['name', 'description', 'cuisine', 'shelf_life']
    template_name = "spice_update.html"
    success_url = "/index/"

class SpicesDelete(DeleteView):
    model = Spices
    template_name = "spice_delete_confirm.html"
    success_url = "/index/"