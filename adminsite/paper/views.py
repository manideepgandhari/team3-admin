from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
#from django.template import loader
# from django.urls import reverse
import requests
from django.core.files.storage import FileSystemStorage
import json
# Create your views here.

def home(request):

    return render(request,'home.html')
def login(request):

    return render(request,'login.html')
def accept(request):
    #this api expects empname and pass to send accesstoken
    #context=requests.post("https://coscmyfirstapitest.herokuapp.com/login",data=request.POST)
    #this context is the access token returned by the api
    #context=context.json()
    #if context.response_code==200:
    return render(request,'uploadpage.html')
    #else:
    #    content={"message":"invalid credentials"}
    #    return render(request,'login.html',content)
def uploadpaper(request):
    if request.method== 'POST':
        data=request.FILES['file']
        other=request.POST.get('username')
        fs=FileSystemStorage()
        name=fs.save(data.name,data)
        url=fs.url(name)
    return HttpResponse(other)

def timetable(request):
    data=request.POST
    return HttpResponse(data)

def check_user_upload(request):
    #context=requests.get("url")
    #context=context.json()
    global ans
    ans=[
    {
        "empno": 7782,
    },
    {
        "empno": 7839
    },
    {
        "empno": 7934
    },
    {
        "empno": 158
    },
    {
        "empno": 7369
    },
    {
        "empno": 7566
    },
    {
        "empno": 7788
    },
    {
        "empno": 7876
    },
    {
        "empno": 7902
    },
    {
        "empno": 1234
    },
    {
        "empno": 7499
    },
    {
        "empno": 7521
    },
    {
        "empno": 7654
    },
    {
        "empno": 7698
    },
    {
        "empno": 7844
    },
    {
        "empno": 7900
    }
    ]

    context={"msg":ans}
    return render(request,'useruploads.html',context)
def getrequestnoinfo(request):
    if request.method=='POST':
        data=request.POST
        global ans
        data=[{"rid":1,"requestno":7782,"img":"image here","more":"coming soon"}]
        context={"msg":ans,"reinfo":data}
        return render(request,'requestinfo.html',context)
def sendrequestinfo(request):
    if request.method=='POST':
        data=request.POST
        #r=requests.post("url",data)
        #r=r.json()
        #if r.status_code==200:
        return render(request,'success.html')

## For both Python 2.7 and Python 3.x
#import base64
#with open("imageToSave.png", "wb") as fh:
#    fh.write(base64.decodebytes(img_data))
ans=[]
