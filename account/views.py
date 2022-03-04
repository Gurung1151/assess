from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.views.generic import CreateView

from .forms import ExamControlBoardSignUpForm, AdminSignUpForm, TeacherSignUpForm,LoginForm
from .models import User,ExamControlBoard,Admin
# Create your views here.

# function views
def mainpage(request):
    return render(request,'main.html')

# admin's portion

def admin_homepage(request):
    #adminObj = Admin.objects.get(id=pk)
    #context = {'adminObj':adminObj}
    return render(request,'account/admin/admin_homepage.html')

# teacher's portion

def teacher_homepage(request):
    #adminObj = Admin.objects.get(id=pk)
    #context = {'adminObj':adminObj}
    return render(request,'account/teacher/teacher_homepage.html')

def teacher_profile(request,pk):
    pass

# ECB's portion
def ECB_homepage(request):
    #adminObj = Admin.objects.get(id=pk)
    #context = {'adminObj':adminObj}
    return render(request,'account/ECB/ECb_homepage.html')


def loginPage(request):
    form = LoginForm(request.POST)
    msg=None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)

            if user is not None and user.is_admin:
                login(request,user)
                return redirect('admin_homepage')
            
            elif user is not None and user.is_teacher:
                login(request,user)
                return redirect('teacher_homepage')

            elif user is not None and user.is_board:
                login(request,user)
                return redirect('ECB_homepage')
            
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'
    context = {'form':form,'msg':msg }
    return render(request, 'account/loginPage.html',context)


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
    