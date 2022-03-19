import django_filters
from .models import *

class ClassFilter(django_filters.FilterSet):
    class Meta:
        model = classData
        fields = '__all__'
        exclude = ['id','subjectName','subjectCode','teacher','batch']