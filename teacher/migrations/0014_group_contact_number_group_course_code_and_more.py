# Generated by Django 5.1.1 on 2024-09-19 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0013_group_group_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='contact_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='course_code',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='duration',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='group',
            name='max_student',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='group',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='start_from',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='lang',
            field=models.CharField(choices=[('1', 'UZ'), ('2', 'RU'), ('3', 'EN')], max_length=20, null=True),
        ),
    ]
