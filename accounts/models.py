from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class AdminManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=CustomUser.Role.ADMIN)

class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        TEACHER = "TEACHER", 'Teacher'
        STUDENT = "STUDENT", 'Student'
    

    base_role = Role.ADMIN
    role = models.CharField(max_length=20, choices=Role.choices)
    admin = AdminManager()
    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


class TeacherManager(BaseUserManager):
    def get_queryset(self,*args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role = CustomUser.Role.TEACHER)


class Teacher(CustomUser):
    base_role = CustomUser.Role.TEACHER
    teacher = TeacherManager()
    class Meta:
        proxy = True
    def welcome(self):
        return "For teachers only"



class StudentManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role = CustomUser.Role.STUDENT)
class Student(CustomUser):
    base_role = CustomUser.Role.STUDENT
    student = StudentManager()
    class Meta:
        proxy = True

    def welcome(self):
        return "For Students Only"



@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'ADMIN':
        AdminProfile.objects.create(user=instance)


class AdminProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    admin_id = models.IntegerField(null=True, blank=True)
