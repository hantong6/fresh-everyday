#-*-coding:utf-8-*-
from django.db import models
from fe_user.models import *
from fe_goods.models import *
# Create your models here.

class OrderInfo(models.Model):
    good=models.ForeignKey(GoodInfo)
    user=models.ForeignKey(UserInfo)
    count=models.IntegerField()
    status=models.BooleanField(default=False)
    isdelete=models.BooleanField(default=False)


