from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    # Main Page Path
    path('', views.Home.as_view(), name="home")
    # Create New Spice Path
    # Individual Spice Route
    # Edit Spice Path
    # Delete Spice Path
]