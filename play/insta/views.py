from django.shortcuts import render
from django.http import HttpResponse
from .models import Database
from . forms import MyForm

# Create your views here.

# def home(request):
#     return HttpResponse("<h1>Hello django</h1>")
# def home1(request):
#     return HttpResponse("<h1>Welcome Mango</h1>")
# def home2(request):
#     return render(request,"index.html")
# def home3(request):
#     return HttpResponse("<h1>Hello Mr Leo Have a nice day</h1>")

def home(request):
    return render(request,'welcome.html')
def welcome(request):
    return render(request,'index.html')

def new(request):
    a=MyForm()
    return render(request,"form.html",{'form':a})

def product (request):
    mobile=request.GET['mobile']
    keyboard=request.GET['keyboard']
    monitor=request.GET['monitor']
    price=request.GET['price']
    myvar=Database(mobile=mobile,monitor=monitor,keyboard=keyboard,price=price)
    myvar.save()
    
    return render (request, 'result.html',{'mobile':mobile, 'keyboard':keyboard, 'monitor':monitor, 'price':price})

def pro (request):
    mobile=request.GET['mobile']
    keyboard=request.GET['keyboard']
    monitor=request.GET['monitor']
    price=request.GET['price']
    myvar=Database(mobile=mobile,monitor=monitor,keyboard=keyboard,price=price)
    myvar.save()
    
    return render (request, 'formresult.html',{'mobile':mobile, 'keyboard':keyboard, 'monitor':monitor, 'price':price})