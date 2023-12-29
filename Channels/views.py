from django.shortcuts import render, HttpResponse


def home(request):
    return HttpResponse("jai shree Ram")