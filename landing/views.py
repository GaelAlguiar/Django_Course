from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

# Create your views here.

def home(req):
    today = date.today()
    stack = [
        {'id':'python', 'name': 'Python'},
        {'id':'flutter', 'name': 'Flutter'},
        {'id':'js', 'name': 'JS'},
        {'id':'nodejs', 'name': 'NodeJs'},
        {'id':'react', 'name': 'React'}
    ]
    return render(req,"landing/landing.html", {
        "name": "Jorge",
        "today": today,
        "age": 21,
        "stack": stack
    })

def stack_detail(req, tool):
    return HttpResponse(f"Tecnología: {tool}")