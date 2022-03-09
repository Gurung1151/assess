from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.

from .models import classData,AssessmentMarks,StudentData

class _Student(admin.ModelAdmin):
    list_display = ['Batch','Dept','Name','Roll'] #Display given fields
    search_fields = ['Batch','Dept','Name']

admin.site.register(classData)
admin.site.register(AssessmentMarks)
admin.site.register(StudentData,_Student)

