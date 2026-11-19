from django.urls import path
from . import views

urlpatterns = [
    path('', views.faculty_list, name='faculty_list'),
    path('add/', views.faculty_add, name='faculty_add'),
]
