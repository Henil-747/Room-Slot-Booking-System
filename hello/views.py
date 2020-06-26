from django.http import HttpResponse
from .models import Request
from django.shortcuts import render,get_object_or_404
from .forms import EventForm
from django.forms import TextInput
from django import forms
from django.contrib.auth.models import User
from django.contrib import messages
def home(request):
        context={}
        return render(request,'hello/homepage.html',context)
def room(request):
    #Request.Username=request.user
    if request.method == 'POST':
        form = EventForm(request.POST)
        if request.POST and form.is_valid():
            form.save()
            messages.success(request, 'Request submitted Successfully')
    else:
        form = EventForm()
    return render(request,'hello/request.html',{'form':form})
