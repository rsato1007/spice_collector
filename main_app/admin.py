from django.contrib import admin
from .models import Spices # import the Artist model from models.py
# Register your models here.

admin.site.register(Spices) # this line will add the model to the admin panel