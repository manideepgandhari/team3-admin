from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
#from django.template import loader
# from django.urls import reverse
import requests
from django.core.files.storage import FileSystemStorage
import json
import base64
from django.conf import settings
import os
# Create your views here.

def login(request):

    return render(request,'login.html')
def home(request):
    #this api expects empname and pass to send accesstoken
    #context=requests.post("https://coscmyfirstapitest.herokuapp.com/login",data=request.POST)
    #this context is the access token returned by the api
    #context=context.json()
    #if context.response_code==200:
    return render(request,'home.html')
    #else:
    #    content={"message":"invalid credentials"}
    #    return render(request,'login.html',content)

def adminpaperpage(request):
    return render(request,'paperuploadform.html')
def admintimetablepage(request):
    return render(request,'ttuploadform.html')
def edittimetablepage(request):
    return render(request,'edittableform.html')


def uploadpaper(request):
    if request.method== 'POST':
        data=request.FILES['file']
        fs=FileSystemStorage()
        name=fs.save(data.name,data)
        basedir=settings.MEDIA_ROOT
        path=os.path.join(basedir,name)
        with open(path,'rb') as img:
            image=base64.b64encode(img.read())
        info=request.POST
        img={"image":image}

        #r=requests.post("apiurl",data=info,img=img)
        #if(r.status_code==200):
        return render(request,'paperuploadform.html',{"message":"Uploaded image successfully"})
        #else:
        #    return render(request,'paperuploadform.html',{"message":"cannot upload something happened"})


def timetable(request):
    data=request.POST
    #r=requests.post("apiurl",data=data)
    #if r.status_code==200:
    return render(request,'ttuploadform.html',{"message":"uploaded timetable successfully"})
    #else:
    #    return render(request,'ttuploadform.html',{"message":"uplod failed something happened"})
def edittable(request):
    data=request.POST
    #r=requests.post("apiurl",data=data)
    #if r.status_code==200:
    return render(request,'edittableform.html',{"message":"edited successfully"})
    #else:
    #return render(request,'edittableform.html',{"message":"edit not successfull"})


def check_user_upload(request):
    #r=requests.get("url")
    #ans=r.json()
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
