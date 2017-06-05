#-*-coding:utf-8-*-
from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class CateGory(models.Model):
    name=models.CharField(max_length=20)
    isdelete=models.BooleanField(default=False)
    def __str__(self):
        return self.name.encode('utf-8')

class GoodInfo(models.Model):
    name=models.CharField(max_length=20)
    pic=models.ImageField(upload_to='goods')
    price=models.DecimalField(max_digits=5,decimal_places=2)
    isdelete=models.BooleanField(default=False)
    weight=models.CharField(max_length=20,default='500g')
    click=models.IntegerField()
    abstract=models.CharField(max_length=200,default='')
    store=models.IntegerField()
    detail=HTMLField()
    category=models.ForeignKey(CateGory)
    def __str__(self):
        return self.name.encode('utf-8')


