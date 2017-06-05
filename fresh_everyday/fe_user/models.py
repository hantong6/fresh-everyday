#-*-coding:utf-8-*-
from django.db import models

# Create your models here.

class UserInfo(models.Model):
    name=models.CharField(max_length=50)
    passwd=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    addressee=models.CharField(max_length=50,default='')
    telephone=models.CharField(max_length=20,default='')
    postcode=models.CharField(max_length=20,default='')
    address=models.CharField(max_length=100,default='')
    def __str__(self):
        return self.name.encode('utf-8')
