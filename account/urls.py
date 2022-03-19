
from django.urls import path,include
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('main/',views.mainpage,name='main'),
    path('',include('classes.urls')),
    
    path('register/Exam_control_board/',views.ExamContolBoardSignUpView.as_view(),name = 'registerECB'),
    path('register/Admin/',views.AdminSignUpView.as_view(),name = 'registerAdmin'),
    path('register/Teacher/',views.TeacherSignUpView,name = 'registerTeacher'),
    
    path('login/',views.loginPage, name='loginPage'),
    path('logout/',views.logoutPage, name='logoutPage'),

    path('Admin/admin_homepage/',views.admin_homepage, name = 'admin_homepage'),
    path('Teacher/teacher_homepage/',views.teacher_homepage, name = 'teacher_homepage'),
    path('Exam_control_board/ECB_homepage/',views.ECB_homepage, name = 'ECB_homepage'),

    path('Teacher/teacher_profile',views.teacher_profile,name='teacher_profile'),
    path('Teacher/teacher_profile_edit',views.editProfile,name='edit_profile'),
    

   path('Admin/teachers/',views.admin_showTeachers,name = 'admin_showTeachers'),
   path('Admin/assessments/',views.admin_assessments,name = 'admin_assessments'),
   path('Admin/teacher/profile/<str:pk>/',views.admin_teacher_profile,name='admin_teacher_profile'),
   path('Admin/assessments/view/<str:pk>/',views.admin_assessment_view,name="admin_assessment_view"),  
   # reset password
   path('reset_password/',auth_views.PasswordResetView.as_view(template_name='account/reset-password.html'),name="reset_password"),
   path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='account/reset-password-done.html'),name="password_reset_done"),
   path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='account/reset-password-confirm.html'),name="password_reset_confirm"),
   path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='account/reset-password-complete.html'),name="password_reset_complete"),

   path('Admin/teacher/assessment/export/<str:pk>/',views.GeneratePdf.as_view(),name='export') 
]