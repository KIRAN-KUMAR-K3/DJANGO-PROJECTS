from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('photos/', views.photos, name='photos'),
    path('forum/', views.forum, name='forum'),
]

