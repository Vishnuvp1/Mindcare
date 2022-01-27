from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage , name='psychologist_home'),
    path('signin/', views.signin, name='psychologist_signin'),
    path('register/', views.register, name='psychologist_register'),
    path('signout/', views.signout , name='psychologist_signout'),
    path('profile/', views.profile , name='psychologist_profile'),
    path('verify/', views.verify , name='psychologist_verify'),
]
