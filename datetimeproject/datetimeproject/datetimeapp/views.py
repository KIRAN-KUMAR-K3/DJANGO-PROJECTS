from django.shortcuts import render
from datetime import datetime


# Create your views here.
def current_datetime(request):
    now = datetime.now()
    return render(request,'datetimeapp/index.html',{'now':now})