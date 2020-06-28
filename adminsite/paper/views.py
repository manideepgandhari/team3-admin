from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
#from django.template import loader
# from django.urls import reverse
import requests
from django.core.files.storage import FileSystemStorage
import json
import base64
from django.conf import settings
import os
#from .models import Store
# Create your views here.

def getsubjectinfo():
    global sub
    r=requests.get("http://127.0.0.1:5000/admin-get-subjects")
    sub=r.json()

def login(request):

    return render(request,'login.html')
def home(request):
    try:
        #this api expects empname and pass to send accesstoken
        context=requests.post("http://127.0.0.1:5000/admin-login",data=request.POST)
        #this context is the access token returned by the api
        context=context.json()
        global accesstoken
        if 'access_token' in context:
            accesstoken=context['access_token']
            accesstoken="Bearer"+" "+str(accesstoken)
            #print(accesstoken)
            getsubjectinfo()
            #store=Store.objects.create(access_token=accesstoken)
            return render(request,'home.html')
        else:
            content={"message":"invalid credentials"}
            return render(request,'login.html',content)
    except:
        return redirect('paper:login')

def adminpaperpage(request):
    global sub
    context={'subject':sub}
    return render(request,'paperuploadform.html',context)
def admintimetablepage(request):
    global sub
    context={'subject':sub}
    return render(request,'ttuploadform.html',context)
def edittimetablepage(request):
    global sub
    context={'subject':sub}
    return render(request,'edittableform.html',context)


def uploadpaper(request):
    try:
        if request.method== 'POST':
            data=request.FILES['image']
            fs=FileSystemStorage()
            name=fs.save(data.name,data)
            basedir=settings.MEDIA_ROOT
            path=os.path.join(basedir,name)
            with open(path,'rb') as img:
                image=base64.b64encode(img.read())
            info=request.POST
            #for including base64 img in the post data
            _mutable=info._mutable
            info._mutable=True
            info['image']=image
            info._mutable=_mutable

            global accesstoken
            header={"Authorization":accesstoken}
            r=requests.post("http://127.0.0.1:5000/admin-qpreq",data=info,headers=header)
            r=r.json()
            #return HttpResponse(r['message'])
            global sub
            context={"msg":r,"subject":sub}
            #if(r['message']=="Succesfully inserted"):
            return render(request,'paperuploadform.html',context)
            #else:
            #    return render(request,'paperuploadform.html',{"message":"cannot upload something happened"})
    except:
        return redirect('paper:home')

def timetable(request):
    try:
        data=request.POST
        global accesstoken
        header={"Authorization":accesstoken}
        #return HttpResponse(data['s_code'])
        r=requests.post("http://127.0.0.1:5000/admin-timetable-create",data=data,headers=header)
        r=r.json()
        #if r.status_code==200:
        global sub
        context={"msg":r,"subject":sub}
        return render(request,'ttuploadform.html',context)
        #else:
        #    return render(request,'ttuploadform.html',{"message":"upload failed something happened"})
    except:
        return redirect('paper:home')
def edittable(request):
    try:
        data=request.POST
        global sub
        global accesstoken
        header={"Authorization":accesstoken}
        r=requests.get("http://127.0.0.1:5000/admin-get-timetable",params=data,headers=header)
        r=r.json()
        try:
            if(r.status_code==200):
                context={"subject":sub,"requestno":r}
                #r={"requestno":6,"subject":sub}
                return render(request,'edittableform2.html',context)
            else:
                context={"subject":sub,"msg":"problem while connecting"}
                return render(request,'edittableform.html',context)
        except:
            context={"subject":sub,"msg":"problem while connecting check details again"}
            return render(request,'edittableform.html',context)
    except:
        return redirect('paper:home')
def sendedittable(request):
    try:
        data=request.POST
        global accesstoken
        header={"Authorization":accesstoken}
        r=requests.post("http://127.0.0.1:5000/admin-timetable-update",data=data,headers=header)
        r=r.json()
        #if(r.status_code==200):
        global sub
        context={"msg":r,"subject":sub}
        return render(request,'edittableform2.html',context)
        #return HttpResponse(data['request_no'])
    except:
        return redirect('paper:edittable')

def check_user_upload(request):
    try:
        global accesstoken
        header={"Authorization":accesstoken}
        r=requests.get("http://127.0.0.1:5000/admin-false-select",headers=header)
        global ans
        ans=r.json()

        context={"msg":ans}
        return render(request,'useruploads.html',context)
    except:
        return redirect('paper:home')
def getrequestnoinfo(request):
    try:
        if request.method=='POST':
            data=request.POST
            global ans
            global accesstoken
            header={"Authorization":accesstoken}
            r=requests.get("http://127.0.0.1:5000/admin-reqno-details",params=data,headers=header)
            r=r.json()
            #data=[{"rid":1,"requestno":7782,"img":"image here","more":"coming soon"}]
            #r=r.json()
            context={"msg":ans,"reinfo":r}
            return render(request,'requestinfo.html',context)
        else:
            return redirect('paper:check_user_upload')
    except:
        return redirect('paper:check_user_upload')
def sendrequestinfo(request):

    if request.method=='POST':
        data=request.POST
        global accesstoken
        header={"Authorization":accesstoken}
        r=requests.post("http://127.0.0.1:5000/admin-delete-req",data=data,headers=header)
        r=r.json()
        #return render(request,'success.html',r)
        return redirect('paper:check_user_upload')

## For both Python 2.7 and Python 3.x
#import base64
#with open("imageToSave.png", "wb") as fh:
#    fh.write(base64.decodebytes(img_data))
ans=[]
sub=[]
accesstoken=""
