# Generated by Django 5.1.1 on 2024-09-16 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_remove_teacher_surname_teacher_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='phone',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]