
from django.urls import path

from .views import ScheduleDeleteView, ScheduleList

urlpatterns = [
    path('', ScheduleList.as_view(), name='schedule_list'),
    path('schedule/<int:pk>/delete/', ScheduleDeleteView.as_view(), name='schedule_delete'),

]


