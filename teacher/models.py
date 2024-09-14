from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Teacher(AbstractUser):
    ...


class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    lang = models.CharField(max_length=20)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}. Language: {self.lang}'


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.BigIntegerField()
    address = models.TextField()
    group = models.ManyToManyField(Group)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.surname}'


class Lesson(models.Model):
    theme = models.CharField(max_length=255)
    date = models.DateField()
    description = models.CharField(max_length=255)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    file = models.FileField(upload_to=f"lessons/{group.name}",)


class Score(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    mark = models.IntegerField(null=False)
    created_at = ...
