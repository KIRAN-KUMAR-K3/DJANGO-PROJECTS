from django.urls import path
from .views import order_notice

urlpatterns = [
    path('', order_notice, name='order_notice'),
]
