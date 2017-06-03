#-*-coding:utf-8-*-
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.core.paginator import Paginator
from models import *
# Create your views here.

def list(request,category_id,pageIndex,orderIndex):
    if orderIndex=='0':
        orderTag='-id'
    elif orderIndex=='1':
        orderTag='price'
    else:
        orderTag='-click'
    category=CateGory.objects.get(id=category_id)
    goodList=GoodInfo.objects.filter(category_id=category_id).order_by(orderTag)
    newList=GoodInfo.objects.filter(category_id=category_id).order_by('-id')[0:2]
    myPaginator=Paginator(goodList,15)
    myPage=myPaginator.page(pageIndex).object_list
    myPageIndex=int(pageIndex)
    myPageNum=myPaginator.num_pages
    context={"category_id":category_id,"category":category,"orderIndex":orderIndex,
             "myPage":myPage,"myPageIndex":myPageIndex,"myPageNum":myPageNum,"newList":newList}
    response=render(request,'./fe_goods/list.html',context)
    response.set_cookie('url',request.get_full_path())
    return response

def detail(request,goodId,category_id):
    category=CateGory.objects.get(id=category_id)
    showGood=GoodInfo.objects.get(id=goodId)
    newList=GoodInfo.objects.filter(category_id=category_id).order_by('-id')[0:2]
    context={'showGood':showGood,'newList':newList,'category_id':category_id,'category':category}
    response=render(request,'./fe_goods/detail.html',context)
    response.set_cookie('url',request.get_full_path())
    return response


