from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.views.generic import CreateView

from .forms import ExamControlBoardSignUpForm, AdminSignUpForm
from .models import User,ExamControlBoard
# Create your views here.

def mainpage(request):
    return render(request,'main.html')

class ExamContolBoardSignUpView(CreateView):
    model = User
    form_class = ExamControlBoardSignUpForm
    template_name = 'account/ECBSignUp.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Exam control board'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        return redirect('main')
    
class AdminSignUpView(CreateView):
    model = User
    form_class = AdminSignUpForm
    template_name = 'account/AdminSignUp.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Admin'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        return redirect('main')