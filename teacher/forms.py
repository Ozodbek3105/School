from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from faker import Faker

from teacher.models import Teacher

fake = Faker()

class AddProfessorForm(UserCreationForm):

    class Meta:
        model = Teacher
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
        required=False, # Make gender optional if needed
        label=''
)

    def __init__(self, *args, **kwargs):
        # Accept initial data from kwargs
        initial = kwargs.get('initial', {})
        
        # Generate fake data if not provided
        initial.setdefault('first_name', fake.first_name())
        initial.setdefault('last_name', fake.last_name())
        initial.setdefault('email', fake.email())
        initial.setdefault('phone', fake.basic_phone_number())
        initial.setdefault('address', fake.address())
        initial.setdefault('gender', fake.random_element(elements=['1', '2']))  # Example gender
        initial.setdefault('department', None)  # Replace with actual default if needed
        initial.setdefault('date_of_birth', fake.date_of_birth(minimum_age=18, maximum_age=65))
        initial.setdefault('education', fake.job())  # Replace with actual default if needed
        initial.setdefault('profile_photo', None)
        initial.setdefault('date_joined', fake.date())
        
        super().__init__(*args, **kwargs)
        self.fields['gender'].choices = [('1', 'Male'), ('2', 'Female')]  # Ensure choices are set

        # Update form's initial data
        self.initial.update(initial)