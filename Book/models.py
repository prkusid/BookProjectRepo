from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

# book related models
class Book(models.Model):

    buser              = models.ForeignKey(User,on_delete=models.CASCADE,)
    bname              = models.CharField(max_length = 50,default='')
    semester           = models.PositiveIntegerField()
    bauthor            = models.CharField(max_length = 30,default='')
    book_available     = models.BooleanField(default=True)
    branch             = models.CharField(max_length =20,default='')
    time               = models.DateTimeField(default=datetime.now(),blank=True)

class UserProfile(models.Model):
    user            = models.OneToOneField(User,on_delete=models.CASCADE)
    mobile_no       = models.CharField(max_length = 15)
    address1        = models.CharField(max_length = 50)
    address2        = models.CharField(max_length = 50)
