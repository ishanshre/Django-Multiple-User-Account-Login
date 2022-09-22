from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'accounts'
urlpatterns = [
    path('', views.UserLoginView.as_view(), name='login'),
    path('index/', views.index, name='index'),
    path('logout/', auth_views.LogoutView.as_view(next_page = 'accounts:login'), name='logout'),
]