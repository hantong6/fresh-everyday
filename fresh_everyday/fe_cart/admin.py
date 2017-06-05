from django.contrib import admin
from models import *
# Register your models here.

class OrderInfoAdmin(admin.ModelAdmin):
    list_display = ['id','good','user','count','status']

admin.site.register(OrderInfo,OrderInfoAdmin)
