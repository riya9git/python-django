from django.shortcuts import render

# Create your views here.

# main/views.py

def home(request):
    return render(request, 'home.html')

