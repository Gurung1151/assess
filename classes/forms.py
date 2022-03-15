from dataclasses import fields
from django import  forms
from django.db import transaction

from .models import classData,AssessmentMarks

# class classForm(forms.ModelForm):
#     class Meta:
#         model = classData
#         fields = '__all__'

class classForm(forms.ModelForm):
    class Meta:
        model = classData
        fields = '__all__'
    @transaction.atomic
    def save(self):
        getClass = super().save(commit=False)
        getClass.save()
        admin_object = AssessmentMarks.objects.create(getClass=getClass)
        admin_object.save()
        return getClass


 

class AssessmentForm(forms.ModelForm):
    class Meta:
        model = AssessmentMarks
        exclude =('FullMarks', 'type', 'is_approved','is_submitted','GetClass')

