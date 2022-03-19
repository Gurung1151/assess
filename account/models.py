from django.db import models

from django.contrib.auth.models import AbstractUser
import uuid

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.

class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_board = models.BooleanField(default=False)
    id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key=True)
    profile_pic = models.ImageField(null = True, blank = True, default="profiles/default.png", upload_to="profiles/")

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    

    def __str__(self):
        return self.user.username

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=20, null = True, blank = True)
    profile_pic = models.ImageField(null = True, blank = True, default="profiles/user-default.png", upload_to="profiles/") 
    #profile_pic

    def __str__(self):
        return self.user.username
    

class ExamControlBoard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=20, null = True, blank = True)

    def __str__(self):
        return self.user.username

class teacherProfile(models.Model):
    user = models.OneToOneField(Teacher,on_delete=models.CASCADE)
    username = models.CharField(max_length=200,null=True,blank=True)
    title = models.CharField(max_length=200,null=True,blank=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(max_length=500,null=True,blank=True)
    phone = models.CharField(max_length=20, null = True, blank = True)
    address =models.CharField(max_length=200, null = True, blank =True)
    bio = models.TextField(null = True, blank = True)
    portfolio_link = models.CharField(max_length=200,null =True, blank =True)
    profile_pic = models.ImageField(null = True, blank = True, default="profiles/default.png", upload_to="profiles/") 
    id = models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True)

    def __str__(self):
        return self.user.user.username

class UserOTP(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    otp = models.IntegerField(null =True, blank=True)

