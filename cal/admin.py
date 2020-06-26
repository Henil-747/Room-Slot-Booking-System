from django.contrib import admin
from cal.models import Event
class EventAdmin(admin.ModelAdmin):
    list_display = ('Room_Number', 'start_time', 'end_time')
admin.site.register(Event,EventAdmin)
# Register your models here.
