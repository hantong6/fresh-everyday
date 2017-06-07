from django.conf.urls import url
import views

urlpatterns=[
    url(r'^cart/$',views.cart),
    url(r'^close_account/$',views.close_account),
    url(r'^new_order(\d+)/$',views.new_order),
    url(r'^del_order(\d+)/$',views.del_order),
    url(r'^chg_count(\d+)-(\d+)/$',views.chg_count),
    url(r'^chg_status(\d+)/$',views.chg_status),
    url(r'^true_status(\d+)/$',views.true_status),
    url(r'^over_order(\d+)/$',views.over_order),
    url(r'^order_submit/$',views.order_submit),
]