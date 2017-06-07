from django.contrib import admin
from models import *
# Register your models here.

class OrderInfoAdmin(admin.ModelAdmin):
    list_display = ['id','good','user','count','status','isdelete']

class PackInfoAdmin(admin.ModelAdmin):
    list_display = ['id','code','order','tmark','isdelete']

admin.site.register(OrderInfo,OrderInfoAdmin)
admin.site.register(PackInfo,PackInfoAdmin)
