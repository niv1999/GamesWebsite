from django.shortcuts import render
from requests import get # pip install requests

from utils.app_config import AppConfig 

# Home view:
def home(request):  # View Function (Request is an object containing request data.)
    context = {"active": "home"}
    return render(request, "home.html", context)


def about(request):
    context = {"active": "about"}
    return render(request, "about.html", context)


def weather(request):
    weatherObject = get(AppConfig.weather_url).json()
    description = weatherObject["weather"][0]["description"]
    temperature = weatherObject["main"]["temp"]

    context = {"active": "weather",
               "description": description,
                "temperature": temperature}
    return render(request, "weather.html", context)
