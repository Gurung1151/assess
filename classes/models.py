from email.policy import default
from operator import mod
from django.db import models
from django.contrib.postgres.fields import ArrayField
import uuid

from django.forms import CharField, IntegerField

from account.models import Teacher

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.

# choices for college year
year_choices = (
    ('I','I'),
    ('II','II'),
    ('III','III'),
    ('IV','IV'),
)
# choices for part of the year of college
part_choices = (
    ('I','I'),
    ('II','II'),
)
# choices for group of the class
group_choices = (
    ('A','A'),
    ('B','B'),
    ('C','C'),
    ('D','D'), 
)

# choices for programme
programme_choices = (
    # ('Computer Engineering','BCT'),
    # ('Electrical Engineering','BEL'),
    # ('Electronic and Communication Engineering','BEX'),
    ('BCT',"BCT"),
    ('BEL',"BEL"),
    ('BEX',"BEX"),
    ('BEI','BEI'),
)

def defArr():
    arr=[]
    for _ in range(24):
        arr =[*arr,0]
    print(arr)
    return arr

class classData(models.Model):
    dept = models.CharField(max_length = 200, choices = programme_choices, null = False, blank = True)
    year = models.CharField(max_length = 200, choices = year_choices, null = False, blank = True )
    part = models.CharField(max_length = 200, choices = part_choices, null = False, blank = True )
    batch = models.CharField(max_length = 200,  null = False, blank = True)
    group = models.CharField(max_length = 200, choices = group_choices, null=True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, editable = False, primary_key = True)
    #Subject = models.ManyToManyField('subject', blank = True)
    subjectName = models.CharField(max_length=200,blank =True,null=True)
    subjectCode = models.CharField(max_length=20,null=True,blank=True)
    #syllabus = models.TextField(blank=True,null=True)
    #subjectAlias = models.CharField(max_length=20,blank=True,null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL,null=True) 
    #is_submitted = models.BooleanField(default=False)
    #is_approved = models.BooleanField(default=False)

    def __str__ (self):
       return self.year + '/' + self.part + '  '+self.batch+self.dept+' '+ self.group +' '+self.subjectName+'-'+self.teacher.__str__()

# class subject(models.Model):
#     subjectName = models.CharField(max_length = 200)
#     syllabus = models.TextField()
#     subjectCode = models.CharField(max_length = 200, blank = True, null = True)
#     #InstructorName = models.CharField(max_length = 200)

#     def __str__(self):
#         return self.subjectName

class AssessmentMarks(models.Model):
    type_choices = (
    ('theory','th'),
    ('practical','Prac'),
    )

    getClass = models.OneToOneField(classData,on_delete=models.DO_NOTHING,primary_key=True)
    dept = models.CharField(max_length = 200, choices = programme_choices, null = False, blank = True)
    year = models.CharField(max_length = 200, choices = year_choices, null = False, blank = True )
    part = models.CharField(max_length = 200, choices = part_choices, null = False, blank = True )
    batch = models.CharField(max_length = 200,  null = False, blank = True)
    group = models.CharField(max_length = 200, choices = group_choices,null=True)
    #Subject = models.ManyToManyField('subject', blank = True)
    subjectName = models.CharField(max_length=200,blank =True,null=True)
    subjectCode = models.CharField(max_length=20,null=True,blank=True)
    #Subject = models.CharField(max_length=200,null=True,blank=True)
    #Teacher =models.ForeignKey(Teacher,on_delete=models.DO_NOTHING,null=True) 
    #Marks = ArrayField(models.IntegerField(null=True,blank=True),size=24,null=True,blank=True,default=[1,2,3])
    #Marks = models.CharField(max_length=48,default='000000000000000000000000000000000000000000000000')
    fullMarks = models.IntegerField(null=True)
    type = models.CharField(max_length = 200 ,choices=type_choices)
    is_approved =models.BooleanField(default=False)
    is_submitted = models.BooleanField(default=False)
    SubmittedMarks1 = models.CharField(max_length=20,null=True,blank=True)
    SubmittedMarks2 = models.CharField(max_length=20,null=True,blank=True)
    SubmittedMarks3 = models.CharField(max_length=20,null=True,blank=True)
    SubmittedMarks4 = models.CharField(max_length=20,null=True,blank=True)
    SubmittedMarks5 = models.CharField(max_length=20,null=True,blank=True)
    SubmittedMarks6 = models.CharField(max_length=20,null=True,blank=True)
    SubmittedMarks7 = models.CharField(max_length=20,null=True,blank=True)
    SubmittedMarks8 = models.CharField(max_length=20,null=True,blank=True)
    SubmittedMarks9 = models.CharField(max_length=20,null=True,blank=True)
    SubmittedMarks10 = models.CharField(max_length=20,null=True,blank=True)
    SubmittedMarks11 = models.CharField(max_length=20,null=True,blank=True)
    SubmittedMarks12 = models.CharField(max_length=20,null=True,blank=True)
    SubmittedMarks13 = models.CharField(max_length=20,null=True,blank=True)
    SubmittedMarks14 = models.CharField(max_length=20,null=True,blank=True)
    SubmittedMarks15 = models.CharField(max_length=20,null=True,blank=True)
    SubmittedMarks16 = models.CharField(max_length=20,null=True,blank=True)
    SubmittedMarks17 = models.CharField(max_length=20,null=True,blank=True)
    SubmittedMarks18 = models.CharField(max_length=20,null=True,blank=True)
    SubmittedMarks19 = models.CharField(max_length=20,null=True,blank=True)
    SubmittedMarks20 = models.CharField(max_length=20,null=True,blank=True)
    SubmittedMarks21 = models.CharField(max_length=20,null=True,blank=True)
    SubmittedMarks22 = models.CharField(max_length=20,null=True,blank=True)
    SubmittedMarks23 = models.CharField(max_length=20,null=True,blank=True)
    SubmittedMarks24 = models.CharField(max_length=20,null=True,blank=True)
    
    def __str__(self):
       return  self.getClass.__str__()+' : '+'Submitted:'+str(self.is_submitted)+',Approved:'+str(self.is_approved)


class StudentData(models.Model):
    Batch = models.CharField(max_length=4,null=True)
    Dept = models.CharField(max_length=3,null=True)
    Roll = models.CharField(max_length=3,null=True)
    Name = models.CharField(max_length=100,null=True)
    Section = models.CharField(max_length=3,null=True)
    def __str__ (self):
        return self.Name

