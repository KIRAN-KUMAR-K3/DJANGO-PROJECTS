from django.shortcuts import render, HttpResponse

# Create your views here.
def show(request):
    return HttpResponse("<h1 > Hello world! </h1>")