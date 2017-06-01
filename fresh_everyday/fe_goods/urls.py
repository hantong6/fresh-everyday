from django.conf.urls import url
import views
urlpatterns=[
    url(r'^list/$',views.list),
    url(r'^detail/$',views.detail),
    url(r'^logout&(\w+)/$',views.logout),



]