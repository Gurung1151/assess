from django.contrib import admin

from .models import User,Teacher,Admin,ExamControlBoard
# Register your models here.

admin.site.register(User)
admin.site.register(Teacher)
admin.site.register(Admin)
admin.site.register(ExamControlBoard)