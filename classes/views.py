from django.shortcuts import render
from django.views.generic import CreateView
# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import StudentData, classData,AssessmentMarks
from .forms import classForm, AssessmentForm
from account.models import Admin
# Create your views here.



# def classes(request) :
#     return HttpResponse("These are classes.")

# def getClass(request):
#     return HttpResponse("This is a specific class.")


# function to render the given html page
def classes(request,pk):
    user = Admin.objects.get(user_id=pk)
    classes = classData.objects.all()
    context = {'classes':classes,'user':user}
    return render(request, 'classes/classes.html',context) 

def getClass(request,pk):
     classObj = classData.objects.get(ID=pk)
     context = {'classObj':classObj}
     return render(request, 'classes/single_class.html', context)
    
# class createClass(CreateView):
#     model = classData
#     form_class = classForm
#     template_name = 'classes/class_form.html'


def createClass(request):
    form = classForm()
    if request.method == 'POST':
        #request.POST
        form = classForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('classes',request.user.id)

    context = {'form':form}
    return render(request,'classes/class_form.html',context)

def updateClass(request,pk):
    getClass = classData.objects.get(ID=pk)
    form = classForm(instance = getClass)
    
    if request.method == 'POST':
        #request.POST
        form = classForm(request.POST, instance = getClass)
        if form.is_valid():
            form.save()
            return redirect('classes')

    context = {'form':form}
    return render(request,'classes/class_form.html',context)

def deleteClass(request,pk):
    getClass = classData.objects.get(ID=pk)
    if request.method == 'POST':
        getClass.delete()
        return redirect('classes')
    context = {'object':getClass}
    return render(request,'classes/delete_template.html',context)

#This is used in assessment  part of the teacher
def teacherAssesments(request):
    classes = AssessmentMarks.objects.all()
    students = StudentData.objects.all()
    context = {'classes':classes,'students':students}
    return render(request,'classes/teacher_assessments.html',context)


# these are not sure
def view_assessment(request,pk):
    marksheet = AssessmentMarks.objects.get(getClass_id = pk)
    students = StudentData.objects.all()
    form = AssessmentForm()
    if request.method=='POST':
        form = AssessmentForm(request.POST)
        if form.is_valid():
            form.save()
            marksheet.is_submitted = True
    context = {'marksheet':marksheet,'students':students,'form':form}
    return render(request,'classes/view_assessment.html',context)

def assessment(request):
    form =AssessmentForm()
    if request.method == 'POST':
        form = AssessmentForm(request.POST)
        if form.is_valid():
            form.save()
            
    context = {'form':form}
    return render(request,'classes/assessment.html',context)

def view(request,pk):
    marks = AssessmentMarks.objects.get(getClass_id=pk)
    students = StudentData.objects.all()
    context = {'marks':marks,'students':students}
    return render(request,'classes/view.html',context)

#For teacher's classes

def teacherClasses(request):
    classes = classData.objects.all().filter(teacher_id=request.user.id)
    context = {'classes':classes}
    return render(request,'classes/teacher_classes.html',context)
