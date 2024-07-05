from django.shortcuts import render

def home(request):
    return render(request, 'main/base.html')

def photos(request):
    return render(request, 'main/photos.html')

def forum(request):
    return render(request, 'main/forum.html')
