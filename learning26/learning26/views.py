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

def recap(request):
     return render(request, "recap.html")

def recipe(request):
     ingredient = ["maggie","tomato"]
     data = {"name":"maggie", "time":20, "ingerdient":ingredient }
     return render(request, "recipe.html",data)  


def iplteam(request):
     playerlist = ["Vk(c)", "Salt", "Rajat", "Paddikal", "Jitesh(wk)", "Timdavid", "Romario", "Pandya", "Suyansh", "Bhuvi", "Josh"]
     dataofteam = {"teamname" : "RCB" , "trophy" : 1 , "captain" : "Virat Kohli", "playerlist" : playerlist}
     return render(request , "iplteam.html", dataofteam)

def collage(request):
     department = ["IT", "COM", "BCA", "MSC", "MBA"]
     dataclg = {"clgname" : "Unique",  "rating" : 4.5, "department":department}
     return render(request, "collage.html", dataclg)