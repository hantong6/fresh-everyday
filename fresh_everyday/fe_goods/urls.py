from django.conf.urls import url
import views
urlpatterns=[
    url(r'^list(\d?)-(\d+)-(\d+)/$',views.list),
    url(r'^detail-(\d+)-(\d?)/$',views.detail),



]