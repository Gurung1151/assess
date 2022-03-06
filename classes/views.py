from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import classData
from .forms import classForm
# Create your views here.

# def classes(request) :
#     return HttpResponse("These are classes.")

# def getClass(request):
#     return HttpResponse("This is a specific class.")


# function to render the given html page
def classes(request):
    classes = classData.objects.all()
    context = {'classes':classes}
    return render(request, 'classes/classes.html',context) 

def getClass(request,pk):
     classObj = classData.objects.get(ID=pk)
     context = {'classObj':classObj}
     return render(request, 'classes/single_class.html', context)
    

def createClass(request):
    form = classForm()
    if request.method == 'POST':
        #request.POST
        form = classForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('classes')

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

def teacherClasses(request):
    classes = classData.objects.all()
    context = {'classes':classes}
    return render(request,'classes/teacherClasses.html',context)
