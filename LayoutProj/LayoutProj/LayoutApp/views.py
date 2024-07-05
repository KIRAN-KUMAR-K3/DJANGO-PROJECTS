from django.shortcuts import render

def home(request):
    return render(request, 'LayoutApp/home.html')

def about(request):
    return render(request, 'LayoutApp/about.html')

def contact(request):
    return render(request, 'LayoutApp/contact.html')
