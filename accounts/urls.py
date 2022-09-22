from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'accounts'
urlpatterns = [
    path('', views.AdminUserLoginView.as_view(), name='login'),
    path('login_student/', views.TeacherUserLoginView.as_view(), name='login_teacher'),
    path('login_teacher/', views.StudentUserLoginView.as_view(), name='login_student'),
    path('index/', views.index, name='index'),
    path('logout/', auth_views.LogoutView.as_view(next_page = 'accounts:login'), name='logout'),
]