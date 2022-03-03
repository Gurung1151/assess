from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.views.generic import CreateView

from .forms import ExamControlBoardSignUpForm, AdminSignUpForm, TeacherSignUpForm
from .models import User,ExamControlBoard
# Create your views here.

# function views
def mainpage(request):
    return render(request,'main.html')


def teacher_profile(request,pk):
    pass

# class views
class ExamContolBoardSignUpView(CreateView):
    model = User
    form_class = ExamControlBoardSignUpForm
    template_name = 'account/ECBSignUp.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Exam control board'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        return redirect('main')
    
class AdminSignUpView(CreateView):
    model = User
    form_class = AdminSignUpForm
    template_name = 'account/AdminSignUp.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Admin'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        #login(self.request,user)
        return redirect('main')

# def register(request):
#     form = RegisterForm(request.POST)
#     msg = None
#     if request.method == 'POST':
        
#         if form.is_valid():
#             user = form.save()
#             msg = "user Created"
#             return redirect('loginPage')
#     return render(request,'account/register.html',{'form':form,'msg':msg})

class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'account/TeacherSignUp.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        #login(self.request,user)
        return redirect('main')
    