from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Ksiazka
from django.template import loader

def ksiazki(request):
    ksiazeczki = Ksiazka.objects.all()
    template = loader.get_template('ksiazki.html')
    context ={
        'ksiazki':ksiazeczki,
    }
    return HttpResponse(template.render(context, request))


