#-*-coding:utf-8-*-
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.core.paginator import Paginator
from models import *
from datetime import datetime
import re
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
    deadLine=datetime(2100,1,1,0,0,0)
    if request.COOKIES.has_key('lastView'):
        lastViewStr=request.COOKIES['lastView']
        result=re.match(r'^(\d+)@(\d+)@(\d+)@(\d+)@(\d+)$',lastViewStr)
        lastView1=GoodInfo.objects.get(id=int(result.group(1)))
        lastView2=GoodInfo.objects.get(id=int(result.group(2)))
        lastView3=GoodInfo.objects.get(id=int(result.group(3)))
        lastView4=GoodInfo.objects.get(id=int(result.group(4)))
        lastView5=GoodInfo.objects.get(id=int(result.group(5)))

        category=CateGory.objects.get(id=category_id)
        showGood=GoodInfo.objects.get(id=goodId)
        showGood.click=showGood.click+1
        showGood.save()
        newList=GoodInfo.objects.filter(category_id=category_id).order_by('-id')[0:2]
        context={'showGood':showGood,'newList':newList,'category_id':category_id,'category':category}
        response=render(request,'./fe_goods/detail.html',context)
        response.set_cookie('url',request.get_full_path())
        response.set_cookie('lastView',str(goodId)+'@'+str(lastView1.id)+'@'+str(lastView2.id)+'@'+str(lastView3.id)+'@'+str(lastView4.id),expires=deadLine)
    else:
        lastView1=GoodInfo.objects.get(id=(int(goodId)-2))
        lastView2=GoodInfo.objects.get(id=(int(goodId)-1))
        lastView3=GoodInfo.objects.get(id=int(goodId))
        lastView4=GoodInfo.objects.get(id=int(goodId)+1)
        lastView5=GoodInfo.objects.get(id=int(goodId)+2)

        category=CateGory.objects.get(id=category_id)
        showGood=GoodInfo.objects.get(id=goodId)
        newList=GoodInfo.objects.filter(category_id=category_id).order_by('-id')[0:2]
        context={'showGood':showGood,'newList':newList,'category_id':category_id,'category':category}
        response=render(request,'./fe_goods/detail.html',context)
        response.set_cookie('url',request.get_full_path())
        response.set_cookie('lastView',str(int(goodId)-2)+'@'+str(int(goodId)-1)+'@'+str(int(goodId))+'@'+str(int(goodId)+1)+'@'+str(int(goodId)+2),expires=deadLine)
    return response




