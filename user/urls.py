from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('service/', views.service, name='service'),
    path('psychologists/', views.psychologists, name='psychologist-list'),
    path('psychologist-details/<int:id>/', views.psychologistdetails, name='psychologist-details'),
    path('payment/', views.payment, name='payment'),
]