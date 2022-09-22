from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import Teacher, Student
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['first_name','last_name', 'username','email']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name','last_name', 'username','email']


class AdminUserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ['username','password']
        

class TeacherUserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)

    class Meta:
        model = Teacher
        fields = ['username','password']
    
    def confirm_login_allowed(self, user):
        if user.role != "TEACHER":
            raise ValidationError(_("Not a teacher account"), code='inactive')

class StudentUserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)

    class Meta:
        model = Student
        fields = ['username','password']