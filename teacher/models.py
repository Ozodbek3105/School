from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

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


class Teacher(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=False, blank=False)
    phone = models.CharField(max_length=100, unique=True, null=True)
    address = models.TextField(null=True)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, null=True, blank=False)
    department = models.ForeignKey('GroupSpec', on_delete=models.CASCADE, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    education = models.CharField(max_length=300, null=True, blank=False)
    profile_photo = models.ImageField(upload_to='professors/profile_photo', null=True, blank=True)

    objects = TeacherManager()

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
   
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class GroupSpec(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Group(models.Model):
    name = models.ForeignKey(GroupSpec, on_delete=models.CASCADE)
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


class Score_Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    mark = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    was_present = models.BooleanField(default=True)


# class Attendance(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)