from typing import Any
from django.contrib.auth import get_user_model
from faker import Faker
from django.contrib.auth.forms import UserCreationForm


fake = Faker()

User = get_user_model()


class AddManagerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", 'phone')

    def save(self, commit: bool = True) -> Any:
        user = super().save(commit=commit)
        user.is_staff = True
        if commit:
            user.save()
        return user
    