from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import AdminUserLoginForm, TeacherUserLoginForm, StudentUserLoginForm
# Create your views here.


class AdminUserLoginView(LoginView):
    form_class = AdminUserLoginForm
    template_name = 'accounts/login.html'


class TeacherUserLoginView(LoginView):
    form_class = TeacherUserLoginForm
    template_name = 'accounts/login.html'
    


class StudentUserLoginView(LoginView):
    form_class = StudentUserLoginForm
    template_name = 'accounts/login.html'

def index(request):
    return render(request, 'accounts/index.html')


