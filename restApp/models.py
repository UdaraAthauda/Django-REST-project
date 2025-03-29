from django.db import models

# Create your models here.

class Student(models.Model):
    student_id = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    employee_id = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.employee_id} - {self.name}"
    
class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_content = models.TextField()

    def __str__(self):
        return self.blog_title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()

    def __str__(self):
        return self.blog.blog_title

