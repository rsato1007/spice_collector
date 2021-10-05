from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    # Main Page Path
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('index/', views.Index.as_view(), name="index"),
    # Create New Spice Path
    path('spices/new/', views.SpicesCreate.as_view(), name="spice_create"),
    # Individual Spice Route
    path('spices/<int:pk>', views.SpicesDetail.as_view(), name="spice_detail"),
    # Edit Spice Path
    path('spices/<int:pk>/update', views.SpicesUpdate.as_view(), name="spice_update"),
    # Delete Spice Path
    path('spices/<int:pk>/delete', views.SpicesDelete.as_view(), name="spice_delete")
]