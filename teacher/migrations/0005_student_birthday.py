# Generated by Django 5.1.1 on 2024-09-21 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_student_profile_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='birthday',
            field=models.DateField(null=True),
        ),
    ]
