from django.shortcuts import render

# Create your views here.

def index(response):
    return render(response, "main/home.html", {})

# def home(response):
#     return render(response, "main/home.html", {})