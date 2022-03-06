from django.urls import  path
from django.urls import include

from . import views

urlpatterns = [

path('Admin/classes',views.classes, name = 'classes'),
path('Admin/class/<str:pk>/',views.getClass, name = 'class'),
path('Admin/create_class/',views.createClass, name = 'create_Class'),
path('Admin/update_class/<str:pk>/',views.updateClass, name = 'update_Class'),
path('Admin/delete_class/<str:pk>/',views.deleteClass, name = 'delete_Class'),

path('Teacher/classes',views.teacherClasses,name='teacherClasses'),

]