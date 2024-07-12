from django.contrib import admin
from django.urls import path
from Myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('image/', views.image_response, name='image'),
    path('pdf/', views.pdf_response, name='pdf'),
    path('csv/', views.csv_response, name='csv'),
    path('zip/', views.zip_response, name='zip'),
    path('plot/', views.plot_response, name='plot'),
 ]