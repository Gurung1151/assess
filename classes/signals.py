from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from classes.views import assessment
from .models import AssessmentMarks,classData

def createAssessment(sender,instance,created,**kwargs):
    if created:
        getClass = instance
        assessment = AssessmentMarks.objects.create(
            getClass = getClass, 
            dept = getClass.dept,
            year = getClass.year,
            part = getClass.part,
            batch = getClass.batch,
            group = getClass.group,
            subjectName = getClass.subjectName,
            subjectCode = getClass.subjectCode

        )

def updateAssessment(sender,instance,created,**kwargs):
    assessment = instance
    getClass = instance.getClass
    if created==False:
        getClass.dept = assessment.dept
        getClass.year = assessment.year
        getClass.part = assessment.part
        getClass.batch = assessment.batch
        getClass.group = assessment.group
        getClass.group = assessment.subjectName
        getClass.group = assessment.subjectCode


# def deleteAsssessment(sender,instance,**kwargs):
#     getClass=instance.getClass
#     getClass.delete()

post_save.connect(createAssessment,sender=classData)
post_save.connect(updateAssessment,sender=AssessmentMarks)
#post_delete.connect(deleteAsssessment,sender=AssessmentMarks)