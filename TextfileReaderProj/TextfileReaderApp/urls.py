from django.urls import path
from . import views
urlpatterns = [
path('', views.form_view, name='form_view'),
path('read_text/', views.read_text, name='read_text'),
]