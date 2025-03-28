from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('students/', views.studentView, name="students"),
    path('employee/', views.Employees.as_view(), name="employee"),
]
