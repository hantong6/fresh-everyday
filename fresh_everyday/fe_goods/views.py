#-*-coding:utf-8-*-
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from models import *
# Create your views here.

def list(request):
    response=render(request,'./fe_goods/list.html')
    response.set_cookie('url',request.get_full_path())
    return response

def detail(request):
    response=render(request,'./fe_goods/detail.html')
    response.set_cookie('url',request.get_full_path())
    return response

def logout(request,tag):
    request.session.flush()
    if tag=='list':
        return redirect('/fe_goods/list/')
    elif tag=='detail':
        return redirect('/fe_goods/detail/')
    else:
        return redirect('/')

