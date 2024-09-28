from typing import Any
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission, Group
from faker import Faker
from django.contrib.auth.forms import UserCreationForm

from django import forms

fake = Faker()

User = get_user_model()


class AddManagerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")

    def save(self, commit: bool = True) -> Any:
        user = super().save(commit=commit)
        user.is_staff = True
        permission_group = Group.objects.get(name='Manager')
        user.groups.add(permission_group)
        if commit:
            user.save()
        return user
