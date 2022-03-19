from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import User,Teacher,Admin,ExamControlBoard,teacherProfile

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
    

    class Meta(UserCreationForm.Meta):
        model = User
    
    def __init__(self, *args, **kwargs) :
        super(TeacherSignUpForm,self).__init__(*args, **kwargs)
    
        for name,  field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
    # @transaction.atomic
    
    # def save(self):
    #  user = super().save(commit=False)
    #  user.is_teacher = True
    #  user.email = self.cleaned_data.get('email')
    #  user.save()
    #  teacher_object = Teacher.objects.create(user=user)
    #  teacher_object.phone = self.cleaned_data.get('phone')
    #  teacher_object.address = self.cleaned_data.get('address')
    #  teacher_object.save()
    #  return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)

    class Meta : 
        model = User

class teacherProfileForm(forms.ModelForm):
    class Meta:
        model= teacherProfile
        fields = ['username','name','title','email','phone','address','phone','bio','portfolio_link','profile_pic']