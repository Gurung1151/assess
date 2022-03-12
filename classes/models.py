from email.policy import default
from operator import mod
from django.db import models
from django.contrib.postgres.fields import ArrayField
import uuid

from django.forms import CharField, IntegerField

from account.models import Teacher
# Create your models here.

# choices for college year
year_choices = (
    ('I','FIRST'),
    ('II','SECOND'),
    ('III','THIRD'),
    ('IV','FOURTH'),
)
# choices for part of the year of college
part_choices = (
    ('I','FIRST'),
    ('II','SECOND'),
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
    group = models.CharField(max_length = 200, choices = group_choices)
    ID = models.UUIDField(default = uuid.uuid4, unique = True, editable = False, primary_key = True)
    #Subject = models.ManyToManyField('subject', blank = True)
    subjectName = models.CharField(max_length=200,blank =True,null=True)
    #syllabus = models.TextField(blank=True,null=True)
    #subjectAlias = models.CharField(max_length=20,blank=True,null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE,null=True) 
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
    #Subject = models.CharField(max_length=200,null=True,blank=True)
    #Teacher =models.ForeignKey(Teacher,on_delete=models.DO_NOTHING,null=True) 
    #Marks = ArrayField(models.IntegerField(null=True,blank=True),size=24,null=True,blank=True,default=[1,2,3])
    #Marks = models.CharField(max_length=48,default='000000000000000000000000000000000000000000000000')
    fullMarks = models.IntegerField(null=False)
    type = models.CharField(max_length = 200 ,choices=type_choices)
    is_approved =models.BooleanField(default=False)
    is_submitted = models.BooleanField(default=False)
    SubmittedMarks1 = models.CharField(max_length=20,null=False,blank=False)
    SubmittedMarks2 = models.CharField(max_length=20,null=False,blank=False)
    SubmittedMarks3 = models.CharField(max_length=20,null=False,blank=False)
    SubmittedMarks4 = models.CharField(max_length=20,null=False,blank=False)
    SubmittedMarks5 = models.CharField(max_length=20,null=False,blank=False)
    SubmittedMarks6 = models.CharField(max_length=20,null=False,blank=False)
    SubmittedMarks7 = models.CharField(max_length=20,null=False,blank=False)
    SubmittedMarks8 = models.CharField(max_length=20,null=False,blank=False)
    SubmittedMarks9 = models.CharField(max_length=20,null=False,blank=False)
    SubmittedMarks10 = models.CharField(max_length=20,null=False,blank=False)
    SubmittedMarks11 = models.CharField(max_length=20,null=False,blank=False)
    SubmittedMarks12 = models.CharField(max_length=20,null=False,blank=False)
    SubmittedMarks13 = models.CharField(max_length=20,null=False,blank=False)
    SubmittedMarks14 = models.CharField(max_length=20,null=False,blank=False)
    SubmittedMarks15 = models.CharField(max_length=20,null=False,blank=False)
    SubmittedMarks16 = models.CharField(max_length=20,null=False,blank=False)
    SubmittedMarks17 = models.CharField(max_length=20,null=False,blank=False)
    SubmittedMarks18 = models.CharField(max_length=20,null=False,blank=False)
    SubmittedMarks19 = models.CharField(max_length=20,null=False,blank=False)
    SubmittedMarks20 = models.CharField(max_length=20,null=False,blank=False)
    SubmittedMarks21 = models.CharField(max_length=20,null=False,blank=False)
    SubmittedMarks22 = models.CharField(max_length=20,null=False,blank=False)
    SubmittedMarks23 = models.CharField(max_length=20,null=False,blank=False)
    SubmittedMarks24 = models.CharField(max_length=20,null=False,blank=False)
    
    def __str__(self):
       return  self.getClass.__str__()+' : '+'Submitted:'+str(self.is_submitted)+',Approved:'+str(self.is_approved)


class StudentData(models.Model):
    Batch = models.CharField(max_length=3,null=True)
    Dept = models.CharField(max_length=3,null=True)
    Roll = models.CharField(max_length=3,null=True)
    Name = models.CharField(max_length=100,null=True)
    Section = models.CharField(max_length=3,null=True)
    def __str__ (self):
        return self.Name

