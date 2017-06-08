#-*-coding:utf-8-*-
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from models import *
from fe_user.models import *
from fe_goods.models import *
from fe_user.decoration import *
import time
# Create your views here.

@jumptologin
def cart(request):
    username=request.session.get('username')
    theUser=UserInfo.objects.get(name=username)
    orderSet=OrderInfo.objects.filter(user_id=theUser.id,status=False)
    context={'orderSet':orderSet}
    return render(request,'./fe_cart/cart.html',context)

def new_order(request,goodId):
    reply={}
    username=request.session.get('username','nobody')
    if username=='nobody':
        reply={'orderCount':0}
    else:
        theUser=UserInfo.objects.get(name=username)
        theGood=GoodInfo.objects.get(id=goodId)
        orderSet=OrderInfo.objects.filter(good_id=goodId,user_id=theUser.id,status=False)
        orderExist=orderSet.count()
        if orderExist==0:
            newOrder=OrderInfo()
            newOrder.good=theGood
            newOrder.user=theUser
            newOrder.count=1
            newOrder.save()
        else:
            theOrder=orderSet[0]
            theOrder.count+=1
            theOrder.save()
        orderCount=OrderInfo.objects.filter(user_id=theUser.id,status=False).count()
        reply={'orderCount':orderCount}
    return JsonResponse(reply)

def del_order(request,delOrderId):
    reply={}
    delOrder=OrderInfo.objects.get(id=delOrderId)
    delOrder.delete()
    return JsonResponse(reply)

def chg_count(request,chgOrderId,newCount):
    reply={}
    chgOrder=OrderInfo.objects.get(id=chgOrderId)
    chgOrder.count=newCount
    chgOrder.save()
    return JsonResponse(reply)

def chg_status(request,chgOrderId):
    reply={}
    chgOrder=OrderInfo.objects.get(id=chgOrderId)
    if chgOrder.status==True:
        chgOrder.status=False
    else:
        chgOrder.status=True
    chgOrder.save()
    return JsonResponse(reply)

def true_status(request,trueOrderId):
    reply={}
    trueOrder=OrderInfo.objects.get(id=trueOrderId)
    trueOrder.status=True
    trueOrder.save()
    return JsonResponse(reply)

def close_account(request,code,isdelete):
    if isdelete=='True':
        return redirect('/fe_user/usercenter_order/')
    else:
        username=request.session.get('username')
        curUser=UserInfo.objects.get(name=username)
        if code=='':
            orderSet2=OrderInfo.objects.filter(user_id=curUser.id,status=True)
            orderSet2=set(orderSet2)
            packSet=PackInfo.objects.all()
            orderSet1=[]
            for pack in packSet:
                orderSet1.append(pack.order)
            orderSet1=set(orderSet1)
            orderSet=orderSet2-orderSet1

            packCode=int(time.time())
            for order in orderSet:
                newPack=PackInfo()
                newPack.code=packCode
                newPack.order=order
                newPack.save()
        else:
            packSet=PackInfo.objects.filter(code=code)
            orderSet=[]
            for pack in packSet:
               orderSet.append(pack.order)
            orderSet=set(orderSet)

        if curUser.address=='':
            context={"orderSet":orderSet,"addressee":"您尚未保存任何收货地址，请添加！","telephone":'',"address":''}
        else:
            context={"orderSet":orderSet,"addressee":'('.decode('utf-8')+curUser.addressee+' 收)'.decode('utf-8'), "telephone": curUser.telephone, "address": curUser.address}
        return render(request,'./fe_cart/place_order.html',context)

def over_order(request,overOrderId):
    reply={}
    overOrder=OrderInfo.objects.get(id=overOrderId)
    overOrder.isdelete=True
    overOrder.save()
    overPack=PackInfo.objects.get(order_id=overOrderId)
    overPack.isdelete=True
    overPack.save()
    return JsonResponse(reply)

def order_submit(request):
    return redirect('/fe_user/usercenter_order/')
