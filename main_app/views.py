from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView

# Create your views here.

# This is what actual serves the home page template
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class Index(TemplateView):
    template_name = "index.html"

# Saving this for reference

# class ArtistList(TemplateView):
#     template_name = "artist_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["artists"] = artists # this is where we add the key into our context object for the view to use
#         return context
