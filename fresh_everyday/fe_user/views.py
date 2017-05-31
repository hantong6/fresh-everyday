#-*-coding:utf-8-*-
from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from hashlib import sha1
from models import *


# Create your views here.

def index(request):
    return render(request,'./fe_user/index.html')

def login(request):
    return render(request,'./fe_user/login.html')

def login_checkname(request,theUser):
    reply={}
    try:
        seekUser=UserInfo.objects.get(name=theUser)
    except:
        reply={"exist":"no"}
    else:
        reply={"exist":"yes"}
    finally:
        return JsonResponse(reply)

def login_checkpasswd(request,theUser,thePasswd):
    reply={}
    shift=sha1()
    shift.update(thePasswd)
    shaPasswd=shift.hexdigest()
    try:
        seekUser=UserInfo.objects.get(name=theUser)
    except Exception:
        pass
    else:
        if seekUser.passwd==shaPasswd:
            reply={"correct":"yes"}
        else:
            reply={"correct":"no"}
    finally:
        return JsonResponse(reply)

def login_submit(request):
    userName=request.POST.get('username')
    userPasswd=request.POST.get('pwd')
    userMark=request.POST.get('usermark')
    response=redirect('/')
    if userMark=='on':
        response.set_cookie('username',userName)
    request.session['username']=userName
    request.session.set_expiry(0)
    return response

def register(request):
    return render(request,'./fe_user/register.html')

def register_checkname(request,newUser):
    reply={}
    try:
        seekUser=UserInfo.objects.get(name=newUser)
    except Exception:
        reply={"exist":"no"}
    else:
        reply={"exist":"yes"}
    finally:
        return JsonResponse(reply)

def register_submit(request):
    newUser=UserInfo()
    newUser.name=request.POST.get('user_name')
    newPwd=request.POST.get('pwd')
    shift=sha1()
    shift.update(newPwd)
    newUser.passwd=shift.hexdigest()
    newUser.email=request.POST.get('email')
    newUser.save()
    return redirect('/fe_user/login/')

def status_check(request):
    username=request.session.get('username','nobody')
    reply={"username":username}
    return JsonResponse(reply)

def usercenter_info(request):
    return render(request,'./fe_user/user_center_info.html')

def usercenter_order(request):
    return render(request,'./fe_user/user_center_order.html')


