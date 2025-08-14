from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class Courses(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    instructor = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    homeworks_count = models.IntegerField(default=1)
    lecture_count = models.IntegerField(default=1)
    laboratory_count = models.IntegerField(default=0)
    final_project_count = models.IntegerField(default=1)

    def __str__(self):
        return self.title
    
class Lecture(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    