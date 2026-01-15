from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

# Create your views here.

def home(req):
    today = date.today()
    return render(req,"landing/landing.html", {
        "name": "Gael",
        "today": today,
        "age":21
    })