from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('service/', views.service, name='service'),
]