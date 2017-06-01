from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

def jumptologin(fun):
    def usercenter(request,*args,**kwargs):
        username=request.session.get('username','nobody')
        if username=='nobody':
            response=redirect('/fe_user/login/')
            response.set_cookie('url',request.get_full_path())
            return response
        else:
            return fun(request,*args,**kwargs)
    return usercenter
