from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepageview(request):
    return render(request,'index.html',{"Name":"Partha"})

def aboutpageview(request):
    return HttpResponse("<h1>About</h1>")

def contactpageview(request):
    return HttpResponse("<h1>Contact</h1>")

def aboutpageview()