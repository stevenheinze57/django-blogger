from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.


def get_home_page(request):
    template = loader.get_template('home/index.html')
    return HttpResponse(template.render())
