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
    video_url = models.URLField()
    sources = models.TextField()
    course = models.ForeignKey(Courses, related_name='lectures', on_delete=models.CASCADE)
    has_lab = models.BooleanField(default=False)
    has_homework = models.BooleanField(default=True)
    homework_description = models.TextField(default='')
    lab_description = models.TextField(default='')

    def __str__(self):
        return f"{self.course.title}"
    
class Homework(models.Model):
    homework_title = models.CharField(max_length=100)
    course = models.ForeignKey(Courses, related_name='homeworks', on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, related_name='lecture', on_delete=models.CASCADE, null=True, blank=True)
    homework_uploaded = models.FileField(upload_to='homeworks/')
    homework_rating = models.IntegerField()
    homework_comment = models.TextField()

    def __str__(self):
        return f"{self.homework_title} - {self.course.title}"