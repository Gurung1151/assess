from dataclasses import fields
from django import  forms


from .models import classData,AssessmentMarks

class classForm(forms.ModelForm):
    class Meta:
        model = classData
        fields = '__all__'


 

class AssessmentForm(forms.ModelForm):
    class Meta:
        model = AssessmentMarks
        exclude =('FullMarks', 'type', 'is_approved','is_submitted','GetClass')

