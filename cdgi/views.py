from django.shortcuts import render
#for call models
from . import models

def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")
def acadmic(request):
    return render(request,"acadmic.html")
def addmision(request):
    return render(request,"addmision.html")
def carrer(request):
    return render(request,"carrer.html")
def contact(request):
    return render(request,"contact.html")
def course(request):
    return render(request,"course.html")
def event(request):
    return render(request,"event.html")
def nacc(request):
    return render(request,"nacc.html")
def placement(request):
    return render(request,"placement.html")
def studentcorner(request):
    return render(request,"studentcorner.html")
