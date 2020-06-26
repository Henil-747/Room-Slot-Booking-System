import datetime
from django.db import models
from django.utils import timezone
from django import forms
from cal.models import Room
from django.contrib.auth.models import User
from django.conf import settings
class Request(models.Model):
    #Username = models.CharField(max_length=50,null=True)
    #Username = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    Room_number= models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    Purpose = models.TextField()
    def __str__(self):
        return str(self.Room_number)