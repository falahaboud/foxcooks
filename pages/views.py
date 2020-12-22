from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def home(request):
    return render(request, 'restaurant/home.html')

def meal(request):
    return render(request, 'restaurant/meal.html')

def order(request):
    return render(request, 'restaurant/order.html')

def report(request):
    return render(request, 'restaurant/report.html')