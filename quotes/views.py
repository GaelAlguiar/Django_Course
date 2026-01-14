from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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

def days_week_number(req, day):
    days = list(days_of_week.keys())
    if(day > len(days)):
        return HttpResponseNotFound("El día no existe")
    redirect_day = days[day-1]
    
    return HttpResponseRedirect(f"/quotes/{redirect_day}")

def days_week(req, day):
    try:
        quote_text = days_of_week[day]
        return HttpResponse(quote_text)
    except:
       return HttpResponseNotFound("Error 404, no se encontró")
    
   