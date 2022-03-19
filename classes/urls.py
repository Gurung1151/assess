from django.urls import  path
from django.urls import include

from . import views

urlpatterns = [
path('Admin/classes/<str:pk>/',views.classes, name = 'classes'),
path('Admin/class/<str:pk>/',views.getClass, name = 'class'),
path('Admin/create_class/',views.createClass, name = 'create_Class'),
path('Admin/update_class/<str:pk>/',views.updateClass, name = 'update_Class'),
path('Admin/delete_class/<str:pk>/',views.deleteClass, name = 'delete_Class'),

#for assessments
path('Teacher/assessments',views.teacherAssesments,name='teacherAssessments'),
path('Teacher/classes/marksheet/<str:pk>/',views.view_assessment,name='marksheet'),

#for teacher's classes
path('Teacher/classes/',views.teacherClasses,name='teacher-classes'),

path('assessment/',views.assessment,name='assessment'),
path('view/<str:pk>/',views.view,name='view'),

]