from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hola Mundo</h1>")

def tablas(request):
    n = 4
    html = "<ul>"
    for i in range(1,13):
        html+=f"<li>{n} * {i} = {n*i}</li>"
        pass
    html += "</ul>"
    return HttpResponse(html)