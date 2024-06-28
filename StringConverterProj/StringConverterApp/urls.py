from django.urls import path
from . import views
urlpatterns = [
path('', views.string_converter_view, name='converter'),
path('quit/', views.quit_view, name='quit'),
]