from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import UserLoginForm
# Create your views here.


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'


def index(request):
    return render(request, 'accounts/index.html')


