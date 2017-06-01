#-*-coding:utf-8-*-
from django.db import models

# Create your models here.

class CateGory(models.Model):
    name=models.CharField(max_length=20)

class GoodInfo(models.Model):
    name=models.CharField(max_length=20)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    weight=models.IntegerField()
    abstract=models.CharField(max_length=100,default='')
    detail=models.CharField(max_length=1000,default='')
    category=models.ForeignKey(CateGory)


