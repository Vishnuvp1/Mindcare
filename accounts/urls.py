from . import views
from django.urls import path

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('register/', views.register, name='register'),
    path('signout/', views.signout, name='signout'),
    path('otp_verify/', views.otp_verify, name='otp_verify')
]
