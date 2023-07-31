from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>İNDEX SAYFASI 10</h1>")


