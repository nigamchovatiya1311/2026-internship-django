from django.http import HttpResponse
from django.shortcuts import render


#specific url

def test(request):
     return HttpResponse("Hello")

def home(request):
     return render(request, "home.html")

def about(request):
     return render(request, "aboutus.html")

def contact(request):
     return render(request, "contactus.html")

def movies(request):
     return render(request, "movies.html")

def shows(request):
     return render(request, "shows.html")

def news(request):
     return render(request, "news.html")     