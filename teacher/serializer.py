import re
from rest_framework import serializers
from rest_framework.validators import ValidationError
from django.contrib.auth.models import Group

from teacher.models import Student, Teacher

class ProfessorSer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', "first_name", "last_name", "email", "phone", "gender")
    
    def save(self, **kwargs):
        print(kwargs)
        print('First name')
        print(self.validated_data)
        data = self.validated_data
        group = Group.objects.get(name='Teacher')
        teacher = super().save(**kwargs)
        teacher.groups.add(group)
        print('First name')
        return teacher


class StudentsSer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', "first_name", "last_name", "email", "phone", "gender")

    def validate_phone(self, phone):
        phone_regex = r"^\+998\s?[0-9]{2}\s?[0-9]{3}[\s?-]?[0-9]{2}[\s?-]?[0-9]{2}$"
        phone_check = re.compile(phone_regex)
        if not phone_check.fullmatch(phone):
            raise ValidationError('Invalid phone number')
        return phone
    