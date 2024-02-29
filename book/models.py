from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
WORKING_HOURS = (
    (datetime.time(hour=11), "11:00"),
    (datetime.time(hour=12), "12:00"),
    (datetime.time(hour=13), "13:00"),
    (datetime.time(hour=14), "14:00"),
    (datetime.time(hour=15), "15:00"),
    (datetime.time(hour=16), "16:00"),
    (datetime.time(hour=17), "17:00"),
    (datetime.time(hour=18), "18:00"),
    (datetime.time(hour=19), "19:00"),
    (datetime.time(hour=20), "20:00"),
    (datetime.time(hour=21), "21:00"),
    (datetime.time(hour=22), "22:00")
 )

possible_number_of_visitors = ((1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7), (8,8), (9,9), (10,10))

possible_number_of_hours = ((1,1), (2,2), (3,3), (4,4), (5,5))


class Schedule(models.Model):
    date_of_visit = models.DateField()
    time_of_visit = models.TimeField(choices = WORKING_HOURS)
    number_of_visitors = models.IntegerField(choices = possible_number_of_visitors)
    number_of_hours = models.IntegerField(choices = possible_number_of_hours)
    visitor = models.ForeignKey(User, on_delete=models.CASCADE)


class Number_of_tables_to_order(models.Model):
    visitor_number = models.IntegerField(unique=True)
    table_number = models.IntegerField()
   