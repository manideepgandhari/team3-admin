from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
#from django.template import loader
# from django.urls import reverse
#from .models import Question,Choice
import requests
# Create your views here.

def home(request):

    return render(request,'home.html')
def login(request):

    return render(request,'login.html')
def accept(request):
    #this api expects empname and pass to send accesstoken
    context=requests.post("https://coscmyfirstapitest.herokuapp.com/login",data=request.POST)
    #this context is the access token returned by the api
    context=context.json()
    if 'accesstoken' in context:
        return render(request,'uploadpage.html')
    else:
        content={"message":"invalid credentials"}
        return render(request,'login.html',content)
def uploadpaper(request):
    data=request.POST
    return HttpResponse(data.json())

def timetable(request):
    data=request.POST

def check_user_upload(request):
    abc=1
