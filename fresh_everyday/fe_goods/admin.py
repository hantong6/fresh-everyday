from django.contrib import admin
from models import *

# Register your models here.

class CateGoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']

class GoodInfoAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','weight','abstract','category']

admin.site.register(CateGory,CateGoryAdmin)
admin.site.register(GoodInfo,GoodInfoAdmin)