from django.db import models
import uuid

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
    ('Computer Engineering','BCT'),
    ('Electrical Engineering','BEL'),
    ('Electronic and Communication Engineering','BEX'),
)

class classData(models.Model):
   
    programme = models.CharField(max_length = 200, choices = programme_choices, null = False, blank = True)
    year = models.CharField(max_length = 200, choices = year_choices, null = False, blank = True )
    part = models.CharField(max_length = 200, choices = part_choices, null = False, blank = True )
    batch = models.CharField(max_length = 200,  null = False, blank = True)
    group = models.CharField(max_length = 200, choices = group_choices)
    created = models.DateTimeField(auto_now_add=True)
    ID = models.UUIDField(default = uuid.uuid4, unique = True, editable = False, primary_key = True )
    #subjects = models.ManyToManyField('subject', blank = True)
    subjectName = models.CharField(max_length=200,blank =True,null=True)
    syllabus = models.TextField(blank=True,null=True)
    subjectAlias = models.CharField(max_length=20,blank=True,null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE,null=True) 
    is_submitted = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

    def __str__ (self):
        return self.year + '/' + self.part + '  '+ self.group

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

    getClass = models.OneToOneField(classData,on_delete=models.CASCADE, primary_key=True)
    #teacher 
    fullMarks = models.IntegerField(null=False)
    type = models.CharField(max_length = 200 ,choices=type_choices)

class StudentData(models.Model):
    Batch = models.CharField(max_length=3,null=True)
    Dept = models.CharField(max_length=3,null=True)
    Roll = models.CharField(max_length=3,null=True)
    Name = models.CharField(max_length=100,null=True)

