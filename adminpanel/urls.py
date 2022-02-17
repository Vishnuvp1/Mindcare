from unicodedata import name
from . import views
from django.urls import path

urlpatterns = [
    path('', views.adminpanel, name='adminpanel'),
    path('admin-login/', views.adminlogin, name='adminlogin'),
    path('user-list', views.userlist, name='userlist'),
    path('psychologistlist', views.psychologistlist, name='psychologistlist'),
    path('guestpsychologist', views.guestpsychologist, name='guestpsychologist'),
    path('adminsignin/', views.adminsignin, name='adminsignin'),
    path('adminsignout/', views.adminsignout, name='adminsignout'),
    path('verifypsychologist/<int:id>/', views.verifypsychologist, name='verifypsychologist')
    
]