from django.urls import path
from get_weather import views

urlpatterns = [
    path('', views.get_meteo, name='get_meteo'),


]