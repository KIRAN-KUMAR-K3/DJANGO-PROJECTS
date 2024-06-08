from django.urls import path
from . import views
urlpatterns = [
    path('', views.input_view, name='input_view'),
]