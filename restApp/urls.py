from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('comments', views.CommentView, basename="comments")
router.register('blogs', views.BlogView, basename="blogs")

urlpatterns = [
    path('', views.index),
    path('students/', views.studentView.as_view(), name="students"),
    path('studentDetail/<int:pk>/', views.studentDetail.as_view(), name="studentDetail"),
    path('employee/', views.Employees.as_view(), name="employee"),
    path('EmployeeDetails/<int:pk>/', views.EmployeeDetails.as_view(), name="EmployeeDetails"),

    path('', include(router.urls)),
]
