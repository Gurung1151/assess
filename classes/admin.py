from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.

from .models import classData,AssessmentMarks,StudentData

admin.site.register(classData)
admin.site.register(AssessmentMarks)
admin.site.register(StudentData)

