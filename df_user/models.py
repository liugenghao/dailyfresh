from django.db import models

# Create your models here.
class Contact(models.Model):
    cname = models.CharField(max_length=20)
    caddress = models.CharField(max_length=100)
    cpostcode = models.CharField(max_length=6)
    cphone = models.CharField(max_length=11)
class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=30)
class UInfo_m2m_contact(models.Model):
    uobj = models.ForeignKey('UserInfo')
    cobj = models.ForeignKey('Contact')