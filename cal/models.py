from django.db import models
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
class Room(models.Model):
    number=models.CharField(max_length=3,null=True)
    def __str__(self):
        return self.number
class Event(models.Model):
    Room_Number=models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    Purpose = models.TextField()
    @property
    def get_html_url(self):
            url = reverse('cal:event_edit', args=(self.id,))
            return f'<a href="{url}"> {str(self.Room_Number)+" "+str(self.start_time)+str(self.end_time)} </a>'
    def __str__(self):
        return str(self.Room_Number)
