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
    # @transaction.atomic
    # def save(self):
    #     getClass = super().save(commit=False)
    #     getClass.save()
    #     admin_object = AssessmentMarks.objects.create(getClass=getClass)
    #     admin_object.save()
    #     return getClass


 

class AssessmentForm(forms.ModelForm):
    class Meta:
        model = AssessmentMarks
        fields = ['SubmittedMarks1','SubmittedMarks1','SubmittedMarks2','SubmittedMarks3','SubmittedMarks4','SubmittedMarks5','SubmittedMarks6','SubmittedMarks7','SubmittedMarks8','SubmittedMarks9',
        'SubmittedMarks10','SubmittedMarks11','SubmittedMarks12','SubmittedMarks13','SubmittedMarks14','SubmittedMarks15','SubmittedMarks16','SubmittedMarks17','SubmittedMarks18',
        'SubmittedMarks19','SubmittedMarks20','SubmittedMarks21','SubmittedMarks22','SubmittedMarks23','SubmittedMarks24']

