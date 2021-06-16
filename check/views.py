from django.shortcuts import render,redirect
from check.models import info
from django.contrib import messages
from check.forms import StudentForm
# Create your views here.
def index(request):
    return render(request,"index.html")

def accept(request):
    form= StudentForm()
    return render(request,'accept.html',{'form':form})

def loginUser(request):
    pass

def logoutUser(request):
    pass
