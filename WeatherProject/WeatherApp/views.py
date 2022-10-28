from django.shortcuts import render
import requests
import datetime

# Create your views here.
def index(request):

    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'bangalore'    




    APPID = 'aea6d42c80e4afdbb0839518a91e864c'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q':'city', 'appid': APPID, 'units':'metric'}
    r = requests.get(url=URL, params=PARAMS)
    res =r.json()
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    # humidity = res['main']['humidity']
    pressure = res['main']['pressure']
    windspeed = res['wind']['speed']
    day = datetime.date.today()

    return render (request, 'index.html', {'description':description, 'icon':icon,
     'temp':temp, 'day':day, 'city':city, 'pressure':pressure,
     'windspeed':windspeed})

def home(request):
    return render(request, 'index.html')

# def aboutme(request):
#     return render(request, 'aboutme.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')