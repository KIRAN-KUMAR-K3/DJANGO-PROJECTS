from urllib import request
from django.http import Http404, HttpResponse
from django.shortcuts import render
from datetime import datetime,timedelta 
import datetime
# views.py
from django.http import HttpResponse
import datetime
def current_date(request):
    now = datetime.datetime.now().date()
    html = f"<html><body><font color=magenta>Today date is {now}.</font></body></html>"
    return HttpResponse(html)
def current_datetime(request):
    now = datetime.datetime.now()
    html = f"<html><body><font color=red>It is now {now}.</font></body></html>"
    return HttpResponse(html)
def hours_ahead(request, offset):
    try:
        offset = int(offset) # Convert the offset to an integer
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
    html = f"<html><body><font color=blue>In {offset} hour(s), it will be {dt}.</font></body></html>"
    return HttpResponse(html)
def hours_before(request, offset):
    try:
        offset = int(offset) # Convert the offset to an integer
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now()-datetime.timedelta(hours=offset)
    html = f"<html><body><font color=brown>Before {offset} hour(s), it was {dt}.</font></body></html>"
    return HttpResponse(html)
