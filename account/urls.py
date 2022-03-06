
from django.urls import path,include
from . import views

urlpatterns = [
    path('main/',views.mainpage,name='main'),
    path('',include('classes.urls')),
    
    path('register/Exam_control_board/',views.ExamContolBoardSignUpView.as_view(),name = 'registerECB'),
    path('register/Admin/',views.AdminSignUpView.as_view(),name = 'registerAdmin'),
    path('register/Teacher/',views.TeacherSignUpView.as_view(),name = 'registerTeacher'),
    
    path('login/',views.loginPage, name='loginPage'),

    path('Admin/admin_homepage/',views.admin_homepage, name = 'admin_homepage'),
    path('Teacher/teacher_homepage/',views.teacher_homepage, name = 'teacher_homepage'),
    path('Exam_control_board/ECB_homepage/',views.ECB_homepage, name = 'ECB_homepage'),

    path('Admin/teachers/',views.admin_showTeachers,name = 'admin_showTeachers'),

]