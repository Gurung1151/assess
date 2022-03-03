
from django.urls import path
from . import views

urlpatterns = [
    path('main/',views.mainpage,name='main'),
    path('register/Exam_control_board/',views.ExamContolBoardSignUpView.as_view(),name = 'registerECB'),
    path('register/Admin/',views.AdminSignUpView.as_view(),name = 'registerAdmin'),
    path('register/Teacher/',views.TeacherSignUpView.as_view(),name = 'registerTeacher'),

]