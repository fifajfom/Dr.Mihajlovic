from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

def Login(request):
    return render(request,'registration/login.html')
