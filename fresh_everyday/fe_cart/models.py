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
    def __str__(self):
        return self.user.name.encode('utf-8')+'/'.encode('utf-8')+self.good.name.encode('utf-8')

class PackInfo(models.Model):
    code=models.IntegerField()
    order=models.ForeignKey(OrderInfo)
    tmark=models.DateTimeField(auto_now_add=True)
    isdelete=models.BooleanField(default=False)



