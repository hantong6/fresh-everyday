#-*-coding:utf-8-*-
from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from hashlib import sha1
from models import *
from decoration import *
from fe_goods.models import *
import re
from haystack.views import SearchView

# Create your views here.

def index(request):
    clickList1=GoodInfo.objects.filter(category_id=1).order_by('-click')[0:3]
    newList1=GoodInfo.objects.filter(category_id=1).order_by('-id')[0:4]
    clickList2=GoodInfo.objects.filter(category_id=2).order_by('-click')[0:3]
    newList2=GoodInfo.objects.filter(category_id=2).order_by('-id')[0:4]
    clickList3=GoodInfo.objects.filter(category_id=3).order_by('-click')[0:3]
    newList3=GoodInfo.objects.filter(category_id=3).order_by('-id')[0:4]
    clickList4=GoodInfo.objects.filter(category_id=4).order_by('-click')[0:3]
    newList4=GoodInfo.objects.filter(category_id=4).order_by('-id')[0:4]
    clickList5=GoodInfo.objects.filter(category_id=5).order_by('-click')[0:3]
    newList5=GoodInfo.objects.filter(category_id=5).order_by('-id')[0:4]
    clickList6=GoodInfo.objects.filter(category_id=6).order_by('-click')[0:3]
    newList6=GoodInfo.objects.filter(category_id=6).order_by('-id')[0:4]
    context={'clickList1':clickList1,'newList1':newList1,
             'clickList2':clickList2,'newList2':newList2,
             'clickList3':clickList3,'newList3':newList3,
             'clickList4':clickList4,'newList4':newList4,
             'clickList5':clickList5,'newList5':newList5,
             'clickList6':clickList6,'newList6':newList6}
    return render(request,'./fe_user/index.html',context)

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
    if request.COOKIES.has_key('url'):
        url=request.COOKIES['url']
        response=redirect(url)
        response.set_cookie('url','',max_age=-1)
    else:
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

def logout(request):
    request.session.flush()
    return redirect('/')

def status_check(request):
    username=request.session.get('username','nobody')
    reply={"username":username}
    return JsonResponse(reply)

@jumptologin
def usercenter_info(request):
    if request.COOKIES.has_key('lastView'):
        lastViewStr=request.COOKIES['lastView']
        result=re.match(r'^(\d+)@(\d+)@(\d+)@(\d+)@(\d+)$',lastViewStr)
        lastView1=GoodInfo.objects.get(id=int(result.group(1)))
        lastView2=GoodInfo.objects.get(id=int(result.group(2)))
        lastView3=GoodInfo.objects.get(id=int(result.group(3)))
        lastView4=GoodInfo.objects.get(id=int(result.group(4)))
        lastView5=GoodInfo.objects.get(id=int(result.group(5)))
        lastList=[lastView1,lastView2,lastView3,lastView4,lastView5]
    else:
        lastList=[]
    username=request.session.get('username')
    curUser=UserInfo.objects.get(name=username)
    if curUser.address=='':
        context={"latsList":lastList,"name":curUser.name,"telephone":'还没有您的联系方式，请在收货地址栏添加！',"address":'还没有您的联系地址，请在收货地址栏添加！'}
    else:
        context={"lastList":lastList,"name":curUser.name,"telephone":curUser.telephone,"address":curUser.address}
    return render(request,'./fe_user/user_center_info.html',context)

@jumptologin
def usercenter_order(request):
    return render(request,'./fe_user/user_center_order.html')

@jumptologin
def usercenter_site(request):
    username = request.session.get('username')
    curUser = UserInfo.objects.get(name=username)
    if curUser.address=='':
        context={"addressee":"您尚未保存任何收货地址，请添加！","telephone":'',"address":''}
    else:
        context={"addressee":'('.decode('utf-8')+curUser.addressee+' 收)'.decode('utf-8'), "telephone": curUser.telephone, "address": curUser.address}
    return render(request,'./fe_user/user_center_site.html',context)

def usercenter_addrsave(request):
    username=request.session.get('username','nobody')
    curUser=UserInfo.objects.get(name=username)
    curUser.addressee=request.POST.get('addressee')
    curUser.telephone=request.POST.get('telephone')
    curUser.address=request.POST.get('address')
    curUser.postcode=request.POST.get('postcode')
    curUser.save()
    context={"addressee":'('.decode('utf-8')+curUser.addressee+' 收）'.decode('utf-8'),"telephone":curUser.telephone,"address":curUser.address}
    return render(request,'./fe_user/user_center_site.html',context)

class FacetedSearchView(SearchView):
    def extra_context(self):
        myPaginator,myPage=super(FacetedSearchView,self).build_page()
        extra=super(FacetedSearchView,self).extra_context()
        extra['pageList']=range(1,myPaginator.num_pages+1)
        return extra

