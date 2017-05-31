from django.conf.urls import url
import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^login/$',views.login),
    url(r'^login_checkname(\w+)/$',views.login_checkname),
    url(r'^login_checkpasswd(\w+)&(\w+)/$',views.login_checkpasswd),
    url(r'^login_submit/$',views.login_submit),
    url(r'^register/$',views.register),
    url(r'^register_checkname(\w+)/$',views.register_checkname),
    url(r'^register_submit/$',views.register_submit),
    url(r'^status_check/$',views.status_check),
    url(r'^usercenter_info/$',views.usercenter_info),
    url(r'^usercenter_order/$',views.usercenter_order),


]