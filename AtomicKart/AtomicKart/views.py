from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome! Hope you have a good day!")