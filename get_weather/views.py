from django.shortcuts import render, redirect
from .forms import MeteoForm
from bs4 import BeautifulSoup
import requests

# Create your views here.
# There was no humidity index in the website

def get_meteo(request):

    if request.method == 'POST':
        form = MeteoForm(request.POST)

        if form.is_valid():
            html_tel_aviv = requests.get(
                "https://www.tameteo.com/meteo_Tel+Aviv-Asie-Israel-Tel+Aviv-LLBG-1-12138.html")
            html_paris = requests.get("https://www.tameteo.com/meteo_Paris-Europe-France-Paris-LFPB-1-26048.html")
            paris = BeautifulSoup(html_paris.text, 'html.parser')
            tel_aviv = BeautifulSoup(html_tel_aviv.text, 'html.parser')

            city = form.cleaned_data['city']
            form = MeteoForm()
            if city.lower() == 'paris':
                location_name = paris.find_all('h1', class_='titulo')[0].text
                temperature = paris.find_all('span', class_='temperatura')[0].text
                windspeed = ''
                for data in paris.find_all('span', class_='uv'):
                    windspeed += f"{data.find_all('span', class_='changeUnitW')[0].text}-{data.find_all('span', class_='changeUnitW')[1].text}"
                probability = paris.find_all('span', class_='probabilidad-lluvia')[0].text
                description = paris.find_all('span', class_='proximas-horas')[0].text
                return render(request, 'get_weather/city.html', {'form': form, 'location_name': location_name, 'temperature': temperature, 'windspeed': windspeed, 'probability': probability, 'description':description})

            elif city.lower() == 'tel aviv':
                location_name = tel_aviv.find_all('h1', class_='titulo')[0].text
                temperature = tel_aviv.find_all('span', class_='temperatura')[0].text
                windspeed = ''
                for wind in tel_aviv.find_all('li', class_='d1'):
                    windspeed += wind.find_all('span', class_='velocidad')[0].text
                probability = tel_aviv.find_all('span', class_='probabilidad-lluvia')[0].text
                description = tel_aviv.find_all('span', class_='proximas-horas')[0].text
                return render(request, 'get_weather/city.html',
                              {'form': form, 'location_name': location_name, 'temperature': temperature, 'windspeed': windspeed, 'probability': probability, 'description':description})

    else:
        form = MeteoForm()
        return render(request, 'get_weather/home.html', {'form': form})



# def city(request, city):
#     html_tel_aviv = requests.get("https://www.tameteo.com/meteo_Tel+Aviv-Asie-Israel-Tel+Aviv-LLBG-1-12138.html")
#     html_paris = requests.get("https://www.tameteo.com/meteo_Paris-Europe-France-Paris-LFPB-1-26048.html")
#     paris = BeautifulSoup(html_paris.text, 'html.parser')
#     tel_aviv = BeautifulSoup(html_tel_aviv.text, 'html.parser')
#
#     if city.lower() == 'paris':
#         location_name = paris.find_all('h1', class_='titulo')[0].text
#         temperature = paris.find_all('span', class_='dato-temperatura')[0].text
#         windspeed = ''
#         for data in paris.find_all('span', class_='uv'):
#             windspeed += f"{data.find_all('span', class_='changeUnitW')[0].text}-{data.find_all('span', class_='changeUnitW')[1].text}"
#             return windspeed
#         return render(request, 'get_weather/city.html',
#                       {'city': city, 'location_name': location_name, 'temperature': temperature,
#                        'windspeed': windspeed})
#
#     elif city.lower() == 'tel aviv':
#         location_name = tel_aviv.find_all('h1', class_='titulo')[0].text
#         temperature = tel_aviv.find_all('span', class_='dato-temperatura')[0].text
#         windspeed = ''
#         for data in tel_aviv.find_all('span', class_='uv'):
#             windspeed += f"{data.find_all('span', class_='changeUnitW')[0].text}-{data.find_all('span', class_='changeUnitW')[1].text}"
#             return windspeed
#
#         return render(request, 'get_weather/city.html',
#                       {'city': city, 'location_name': location_name, 'temperature': temperature,
#                        'windspeed': windspeed})
#     return render(request,''