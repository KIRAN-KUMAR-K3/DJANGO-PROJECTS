# urls.py in FeedbackApp
from django.urls import path
from .views import contact, success
from FeedbackApp import admin, views

urlpatterns = [
    path('', contact, name='contact'),
    path('success/', success, name='success'),
]
