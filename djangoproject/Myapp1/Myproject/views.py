from django.http import HttpResponse
from django.shortcuts import render

def homepage (request):
    data={'Title':'Home Page New'

    }
    return render(request,"index.html",data):

def course(request):
    return HttpResponse("Welcome to new age E-Commerce")
    

def homepage (request):
    return render("Welcome to Myproject")

def homepage (request):
    return render("Welcome to Myproject")
