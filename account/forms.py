from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import User,Teacher,Admin,ExamControlBoard

class ExamControlBoardSignUpForm(UserCreationForm):
    phone = forms.CharField(max_length=20,required=False)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_board = True
        user.save()
        ECB_object = ExamControlBoard.objects.create(user=user)
        ECB_object.phone = self.cleaned_data.get('phone')
        ECB_object.save()
        return user
    
class AdminSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=20,required=False)
   

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = True
        user.email = self.cleaned_data.get('email')
        user.save()
        admin_object = Admin.objects.create(user=user)
        admin_object.phone = self.cleaned_data.get('phone')
        admin_object.save()
        return user

class TeacherSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=20, required=False)
    address =forms.CharField(max_length=200, required=False)

    class Meta(UserCreationForm.Meta):
        model = User
    
    
    @transaction.atomic
    
    def save(self):
     user = super().save(commit=False)
     user.is_teacher = True
     user.email = self.cleaned_data.get('email')
     user.save()
     teacher_object = Teacher.objects.create(user=user)
     teacher_object.phone = self.cleaned_data.get('phone')
     teacher_object.address = self.cleaned_data.get('address')
     teacher_object.save()
     return user