from django.contrib import admin
from django.urls import path, include
from . import views
from django.http import HttpResponse


urlpatterns = [
    path('', views.index ),
    path('list_staff/', views.list_staff),
    path('list_staff/<int:employee_id>/', views.staff_detail),
    path('list_students/', views.list_students),
    path('list_students/<int:school_id>/', views.student_detail)
]
