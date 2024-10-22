from dataclasses import fields
import re
from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from faker import Faker
from django.contrib.auth import get_user_model
from django.forms import ValidationError, modelformset_factory
from django.db import models
from teacher.models import   Group, GroupSpec, Lesson, Score_Attendance, Skill, Student
from django.contrib.auth.models import Group as GroupType
from teacher.models import Group, GroupSpec, Lesson, Score_Attendance, Student

fake = Faker()

User = get_user_model()


class AddProfessorForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'gender', 
                  'department', 'date_of_birth', 'education', 'profile_photo', 'date_joined']

        widgets = {
            'gender': forms.Select,
            # 'date_joined': forms.DateInput,
            # 'date_of_birth': forms.DateInput(attrs={"type": "datetime-local"}),
            # 'profile_photo': forms.ClearableFileInput(attrs={'class': 'dropify'}),
        }

    gender = forms.ChoiceField(
        choices=[('1', 'Male'), ('2', 'Female')],
        widget=forms.Select,
        required=True, # Make gender optional if needed
        label=''
)

    # def __init__(self, *args, **kwargs):
    #     # Accept initial data from kwargs
    #     initial = kwargs.get('initial', {})
        
    #     # Generate fake data if not provided
    #     initial.setdefault('first_name', fake.first_name())
    #     initial.setdefault('last_name', fake.last_name())
    #     initial.setdefault('email', fake.email())
    #     initial.setdefault('phone', fake.basic_phone_number())
    #     initial.setdefault('address', fake.address())
    #     initial.setdefault('gender', fake.random_element(elements=['1', '2']))  # Example gender
    #     initial.setdefault('department', None)  # Replace with actual default if needed
    #     initial.setdefault('date_of_birth', fake.date_of_birth(minimum_age=18, maximum_age=65))
    #     initial.setdefault('education', fake.job())  # Replace with actual default if needed
    #     initial.setdefault('profile_photo', None)
    #     initial.setdefault('date_joined', fake.date())
        
    #     super().__init__(*args, **kwargs)
    #     self.fields['gender'].choices = [('1', 'Male'), ('2', 'Female')]  # Ensure choices are set

    #     # Update form's initial data
    #     self.initial.update(initial)
    
    def save(self, commit = True):
        user = super().save(commit)
        group = GroupType.objects.get(name='Teacher')
        user.groups.add(group)
        if commit:
            user.save()
        return user
    
    def clean_phone(self):
        phone = self.cleaned_data.get("phone", '')
        phone_regex = r"^(\+998\s?)?[0-9]{2}\s?[0-9]{3}[\s?-]?[0-9]{2}[\s?-]?[0-9]{2}$"
        phone_check = re.compile(phone_regex)
        if not phone_check.fullmatch(phone):
            raise ValidationError('Invalid phone number')
        return phone


class EditProfessorForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'gender', 
                  'department', 'date_of_birth', 'education', 'profile_photo', 'date_joined']

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': "New Password", "type": "password"}),
        label="New Passwor",
        required=False,
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm New Password", 'type': 'password'}),
        label="Confirm New Password",
        required=False
    )

    def clean_phone(self):
        phone = self.cleaned_data.get("phone", '')
        phone_regex = r"^(\+998\s?)?[0-9]{2}\s?[0-9]{3}[\s?-]?[0-9]{2}[\s?-]?[0-9]{2}$"
        phone_check = re.compile(phone_regex)
        if not phone_check.fullmatch(phone):
            raise ValidationError('Invalid phone number')
        return phone

    def clean(self) -> dict[str, Any]:
        clean_data = super().clean()
        password1 = clean_data.get("password1", '')
        password2 = clean_data.get("password2", '')
        print(clean_data)
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError('Password does not match')
        
        return clean_data
    
    def save(self, commit: bool = True) -> Any:
        user = super().save(commit=False)
        if self.cleaned_data.get('password1') and self.cleaned_data.get('password2'):
            user.set_password(self.cleaned_data.get('password2'))
        if commit:
            user.save()
        return user

    gender = forms.ChoiceField(
        choices=[('1', 'Male'), ('2', 'Female')],
        widget=forms.Select,
        required=False, # Make gender optional if needed
        label=''
        )


class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('name', 'course_code', 'description', 'start_from', 'duration', 'price', 'teacher', 'max_student', 'contact_number', 'lang', 'group_photo')


class AddStudentForm(forms.ModelForm):  
    class Meta:
        model = Student
        fields = ("first_name", "last_name","surname","email","phone","address","group","education","profile_photo","gender","birthday")
        widgets = {
            "gender":forms.Select
        }

    gender = forms.ChoiceField(
        choices=[('1', 'Male'), ('2', 'Female')],
        widget=forms.Select,
        required=True, # Make gender optional if needed
        label=''
        )
    
    def clean_phone(self):
        phone = self.cleaned_data.get("phone", '')
        phone_regex = r"^(\+998\s?)?[0-9]{2}\s?[0-9]{3}[\s?-]?[0-9]{2}[\s?-]?[0-9]{2}$"
        phone_check = re.compile(phone_regex)
        if not phone_check.fullmatch(phone):
            raise ValidationError('Invalid phone number')
        return phone
    

class EditStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("first_name", "last_name", "email", "phone", "address", "group", "profile_photo", "gender")

    def clean_phone(self):
        phone = self.cleaned_data.get("phone", '')
        phone_regex = r"^(\+998\s?)?[0-9]{2}\s?[0-9]{3}[\s?-]?[0-9]{2}[\s?-]?[0-9]{2}$"
        phone_check = re.compile(phone_regex)
        if not phone_check.fullmatch(phone):
            raise ValidationError('Invalid phone number')
        return phone
    
    gender = forms.ChoiceField(
        choices=[('1', 'Male'), ('2', 'Female')],
        widget=forms.Select,
        required=False, # Make gender optional if needed
        label=''
        )


class AddLessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'


class EditLessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'


# class AttendanceForm(forms.ModelForm):
#     class Meta:
#         model = Score_Attendance
#         fields = ["student", 'lesson', 'mark', 'is_present']

StudentsAttendanceFormSet = modelformset_factory(model=Score_Attendance, fields=["student", 'lesson', 'mark', 'is_present'], extra=0)


class AddDepartmentForm(forms.ModelForm):
    class Meta:
        model = GroupSpec
        fields = ['name','description']


class AddSkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = "__all__"


class EditSkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = "__all__"