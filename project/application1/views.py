from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World")

def function(request):
    return render(request,'data.html',{'name':'raju'})


def add1(request):
    a=int(request.GET["num1"])
    b=int(request.GET["num2"])
    c=a+b
    return render(request,'result.html',{'name':c})    