from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
days_of_week = {
    "monday": "Pienso, luego existo",
    "tuesday": "La vida es un sueño",
    "wednesday": "El conococimineto es poder",
    "thursday": "Se el cambio que quieres ver",
    "friday": "Solo se que no se nada",
    "saturday": "Vive como si fuera el ultimo dia",
    "sunday": "Da un poquito más todos los días"
}


def index(req):
    days = list(days_of_week.keys())  # [Monday, Tuesday ...]

    return render(req, "quotes/quotes.html", {
        "days": days
    })


def days_week_number(req, day):
    days = list(days_of_week.keys())

    if day < 1 or day > len(days):
        return render(req, "quotes/day_quotes.html", {
            "invalid_day": True
        })

    day_name = days[day - 1]
    quote = days_of_week[day_name]

    return render(req, "quotes/day_quotes.html", {
        "day_name": day_name,
        "quote": quote,
    })


def days_week(req, day):
    try:
        quote_text = days_of_week[day]
        return HttpResponse(quote_text)
    except Exception:
        return HttpResponseNotFound("Error 404, no se encontró")
