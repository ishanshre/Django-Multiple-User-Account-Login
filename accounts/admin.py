from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth import get_user_model
from .models import Teacher, Student
# Register your models here.

@admin.register(get_user_model())
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username','email','is_staff']
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = UserAdmin.add_fieldsets

@admin.register(Teacher)
class CustomTeacherUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username','email','is_staff']
    fieldsets = UserAdmin.fieldsets + ((None,{'fields':('role',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None,{'fields':('role',)}),)

@admin.register(Student)
class CustomStudentUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username','email','is_staff']
    fieldsets = UserAdmin.fieldsets + ((None,{'fields':('role',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None,{'fields':('role',)}),)