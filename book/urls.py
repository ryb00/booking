from . import views
from django.urls import path

urlpatterns = [
    path('', views.ScheduleList.as_view(), name='home'),
]


