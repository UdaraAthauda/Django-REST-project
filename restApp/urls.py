from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('students/', views.studentView.as_view(), name="students"),
    path('studentDetail/<int:pk>/', views.studentDetail.as_view(), name="studentDetail"),
    path('employee/', views.Employees.as_view(), name="employee"),
    path('EmployeeDetails/<int:pk>/', views.EmployeeDetails.as_view(), name="EmployeeDetails"),
]
