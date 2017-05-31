from django.contrib import admin
from models import *

# Register your models here.

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['id','name']

admin.site.register(UserInfo,UserInfoAdmin)
