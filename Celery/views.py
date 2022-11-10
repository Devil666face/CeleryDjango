from django.shortcuts import render
from django.http import HttpResponse
from .tasks import download


def home(request):
    download.delay()
    return HttpResponse("<h1>Гружу</h1>")