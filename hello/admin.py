from django.contrib import admin
from .models import Request
class RequestAdmin(admin.ModelAdmin):
    list_display = ('Room_number', 'start_time', 'end_time',)
admin.site.register(Request,RequestAdmin)

# Register your models here.
