import os
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import Group, PermissionsMixin
from requests import delete


# Create your models here.


class TeacherManager(BaseUserManager):

    def create_user(self, first_name, last_name, email, phone=None, address=None, password=None, gender=None, department=None, date_of_birth=None, education=None, date_joined=None):
        if not email:
            raise ValueError('Invalid email')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            address=address,
            gender=gender,
            department=department,
            date_of_birth=date_of_birth,
            education=education,
            date_joined=date_joined
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, password):
        if not email:
            raise ValueError('Email is required')

        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )

        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)

        return user


GENDER_CHOICES = (
    ('1', 'Male'),
    ('2', 'Female')
)


class Teacher(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=False, blank=False)
    phone = models.CharField(max_length=100, unique=True, null=True)
    address = models.TextField(null=True, blank=True)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, null=True, blank=False, )
    department = models.ForeignKey('GroupSpec', on_delete=models.CASCADE, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    education = models.CharField(max_length=300, null=True, blank=False)
    profile_photo = models.ImageField(upload_to='professors/profile_photo', null=True, blank=True)
    skills = models.ManyToManyField('Skill', blank=True)

    objects = TeacherManager()

    date_joined = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def delete(self, using =None, keep_parents =False):
        if self.profile_photo:
            path = self.profile_photo.path
            if path:
                os.remove(path)
        return super().delete(using, keep_parents)

    # class Meta:
    #     permissions = [
    #         ('add_professor', 'Can add a professor'),
    #         # add other custom permissions if necessary
    #     ]


class Skill(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.name}'


class GroupSpec(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'


LANG_CHOICES = (
    ("1", "UZ"),
    ("2", "RU"),
    ("3", "EN"),
)


class Group(models.Model):
    name = models.ForeignKey(GroupSpec, on_delete=models.CASCADE)
    course_code = models.CharField(max_length=100, null=True)
    description = models.TextField()
    start_from = models.DateField(null=True)
    duration = models.IntegerField(default=3)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    max_student = models.IntegerField(default=10)
    contact_number = models.CharField(max_length=100, null=True)
    lang = models.CharField(max_length=20, choices=LANG_CHOICES, null=True)
    group_photo = models.ImageField(upload_to='courses/course_photo/%Y/%m', null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}. Language: {self.lang}'

    def delete(self, using =None, keep_parents =False):
        if self.group_photo:
            path = self.group_photo.path
            if path:
                os.remove(path)
        return super().delete(using, keep_parents)


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.TextField()
    profile_photo = models.ImageField(upload_to='studnet/profile_photo', null=True, blank=True)
    group = models.ManyToManyField(Group)
    education = models.CharField(max_length=300, null=True, blank=False)
    gender = models.CharField(max_length=20, null=True, blank=False, choices=GENDER_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    birthday = models.DateField(null=True) 
    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.surname}'

    def delete(self, using = ..., keep_parents = ...):
        if self.profile_photo:
            path = self.profile_photo.path
            os.remove(path)
        return super().delete(using, keep_parents)


def lesson_file_upload_path(instance, file_name):
    if instance.lesson.group.name.name:
        return f"lessons/{instance.lesson.group.name.name}/{file_name}"
    else:
        group_name = 'Unknown'
        return f"lessons/{group_name}/{file_name}"
    

class Lesson(models.Model):
    theme = models.CharField(max_length=255)
    date = models.DateField()
    description = models.CharField(max_length=255)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.theme}"

class LessonFiles(models.Model):
    file = models.FileField(null=True, blank=True, upload_to=lesson_file_upload_path)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.file.name}'
    
    # def delete(self, using =None, keep_parents =False):
    #     if self.file:
    #         file_path = self.file.path
    #         if file_path:
    #             os.remove(file_path)
    #     return super().delete(using, keep_parents)

    class Meta:
        verbose_name_plural = "LessonFiles"


class Score_Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    mark = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    was_present = models.BooleanField(default=True)


# class Attendance(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     lesson = models.ForeignKey(Lesson,  on_delete=models.CASCADE)


class GroupLikes(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    session_id = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.user.first_name}'
