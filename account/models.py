from django.db import models

from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.

class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_board = models.BooleanField(default=False)
    id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key=True)

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=20, null = True, blank = True)
    address =models.CharField(max_length=200, null = True, blank =True)
    bio = models.TextField(null = True, blank = True)
    portfolio_link = models.CharField(max_length=200,null =True, blank =True)
    profile_pic = models.ImageField(null = True, blank = True, default="profiles/user-default.png", upload_to="profiles/") 

    def __str__(self):
        return self.user.username

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=20, null = True, blank = True)
    #profile_pic

    def __str__(self):
        return self.user.username
    

class ExamControlBoard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=20, null = True, blank = True)

    def __str__(self):
        return self.user.username
    