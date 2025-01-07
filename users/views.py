from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

def register(request):
    form = UserCreationForm()
    return render(request,'users/register.html',{'form':form})
    