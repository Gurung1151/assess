from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.views.generic import CreateView

from .forms import ExamControlBoardSignUpForm, AdminSignUpForm, TeacherSignUpForm,LoginForm,teacherProfileForm
from .models import Teacher, User,ExamControlBoard,Admin, UserOTP, teacherProfile
from classes.models import StudentData,AssessmentMarks,classData

import random

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail

from django.contrib.auth.decorators import login_required

import classes

from django.template.loader import render_to_string
from django.views.generic import View

from .export2pdf import html_to_pdf 
from django.http import HttpResponse

# Create your views here.

# function views
def mainpage(request):
    text = 'Hello, this is temporary main page'
    students = StudentData.objects.all()
    context = {'text':text,'students':students}
    return render(request,'main.html',context)

# admin's portion

def admin_homepage(request):
    approvals = AssessmentMarks.objects.all().filter(is_approved=False,is_submitted=True)
    approvalsCount = AssessmentMarks.objects.all().filter(is_approved=False,is_submitted=True).count()
    context = {'approvals':approvals,'approvalsCount':approvalsCount}
    return render(request,'account/admin/admin_homepage.html',context)

def admin_assessments(request):
    assessments = AssessmentMarks.objects.all().filter(is_submitted=True)
    context={'assessments':assessments}
    return render(request,'account/admin/admin_assessments.html',context)

def admin_showTeachers(request):

    teachers = teacherProfile.objects.all()
    context = {'teachers':teachers}
    return render(request, 'account/admin/admin_showTeachers.html',context)

# teacher's portion

def admin_teacher_profile(request,pk):
    teacher = teacherProfile.objects.get(id=pk)
    classes = classData.objects.all().filter(teacher_id=teacher.user_id)
    context = {'teacher':teacher,'classes':classes}
    return render(request,'account/admin/admin_teacher_profile.html',context)

def teacher_homepage(request):
    submitted = AssessmentMarks.objects.all().filter(is_submitted = True)
    not_submitted = AssessmentMarks.objects.all().filter(is_submitted = False)
    context = {'submitted': submitted, 'not_submitted':not_submitted}
    return render(request,'account/teacher/teacher_homepage.html',context)

@login_required(login_url="loginPage") 
def teacher_profile(request):
    teacher = teacherProfile.objects.get(user_id=request.user.id)
    context = {'teacher':teacher}
    return render(request,'account/teacher/teacher_profile.html',context)

@login_required(login_url='loginPage')
def editProfile(request):
    
    teacher = teacherProfile.objects.get(user_id=request.user.id)
    form = teacherProfileForm(instance=teacher)
    if request.method == 'POST':
        form = teacherProfileForm(request.POST,request.FILES,instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_profile')
    context = {'form':form}
    return render(request,'account/teacher/teacher_profile_form.html',context)

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

def logoutPage(request):
    logout(request)
    return redirect('loginPage')


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

# class TeacherSignUpView(CreateView):
#     model = User
#     form_class = TeacherSignUpForm
#     template_name = 'account/TeacherSignUp.html'

#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'teacher'
#         return super().get_context_data(**kwargs)
    
#     def form_valid(self, form):
#         user = form.save()
#         #login(self.request,user)
#         return redirect('main')
    
def TeacherSignUpView(request):
    if request.method == 'POST':
        get_otp = request.POST.get('otp')

        if get_otp:
            get_user = request.POST.get('user')
            user = User.objects.get(username=get_user)
            
            if int(get_otp)==UserOTP.objects.filter(user=user).last().otp:
                user.is_active = True
                user.save()
                messages.success(request,f'Account is created for {user.username}')
                return redirect('loginPage')
            else:
                messages.error(request,f'Sorry!!! You Have Entered Wrong OTP')
                return render(request, 'account/TeacherSignUp.html',{'otp':True,'user':user})
        
        
        form = TeacherSignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            user = User.objects.get(username=username)
            user.is_teacher = True
            user.is_active = False
            user.email = email
            user.save()
            teacher_obj = Teacher.objects.create(user=user)
            teacher_obj.save()

            #otp part
            user_otp = random.randint(100000,999999)
            UserOTP.objects.create(user=user,otp=user_otp)
            msg = f'Hello {user.username},\n Your OTP is {user_otp}\n Thank You For Signing Up'

            send_mail(
                'Verify Your Email',
                msg,
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently = False
            )

            return render(request, 'account/TeacherSignUp.html',{'otp':True,'user':user})

            #return redirect('loginPage')
    
    else:
        form = TeacherSignUpForm()
    
    context = {'form':form}
    return render(request,'account/TeacherSignUp.html',context)

def admin_assessment_view(request,pk):
    assessment = AssessmentMarks.objects.get(getClass_id=pk)
    
    students = StudentData.objects.all().filter(Dept=assessment.dept,Batch=assessment.batch,Section=assessment.group)
    context = {'assessment':assessment,'students':students}
    return render(request,'account/admin/admin_assessment_view.html',context)   

class GeneratePdf(View):
     def get(self, request,pk, *args, **kwargs):
         
        # getting the template
        asmtStats = AssessmentMarks.objects.get(getClass_id = pk)
        studentList = StudentData.objects.filter(Batch = asmtStats.getClass.batch,Dept=asmtStats.getClass.dept,Section=asmtStats.getClass.group)
        MarkList = [getattr(asmtStats,'SubmittedMarks'+str(i+1)) for i in range(24)]
        RemarkList = []
        for i in MarkList:
        #    if(i<asmtStats.PassMarks):
        #        RemarkList.append('Fail')
        #    elif(i>asmtStats.fullMarks):
        #        RemarkList.append('More than FM')
        #    elif(i=0):
        #        RemarkList.append('Absent')
        #    else:
                RemarkList.append(' ')
        CompleteData =[]
        flag=0
        for i in (studentList):
            temp = {'Name': i.Name,
                    'CRN':i.Batch+i.Dept+i.Roll,
                    'Marks': MarkList[flag],
                    'Remarks':RemarkList[flag]
                    }
            flag+=1
            CompleteData.append(temp);
          

        print(CompleteData)
        context ={'asmtStats' : asmtStats , 'CompleteData' : CompleteData}
        open('account/templates/account/temp.html', "w").write(render_to_string('account/final_export.html',context ))
        pdf = html_to_pdf('account/temp.html')
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')