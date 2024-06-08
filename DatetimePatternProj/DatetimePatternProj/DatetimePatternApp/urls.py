from django.urls import path,re_path
from .views import current_date, current_datetime,hours_ahead, hours_before
from DatetimePatternApp import views
urlpatterns = [
    path('', current_date),
    re_path(r'^time/', current_datetime),
    re_path(r'^ctime/plus/(\d{1,2})/$', hours_ahead),
    re_path(r'^ctime/minus/(\d{1,2})/$', hours_before),
 ]