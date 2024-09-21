from django import forms
from django.contrib import admin

from teacher.models import Group, GroupLikes, GroupSpec, Lesson, Score_Attendance, Skill, Student, Teacher, TeacherManager

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

        widgets = {
            "group": forms.CheckboxSelectMultiple
        }


class StudentAdmin(admin.ModelAdmin):
    form = StudentForm
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone', 'gender', 'created_at']
    ordering = ("id", "first_name", "last_name", "group")
    sortable_by = ("gender",)
    list_display_links = ['id', 'first_name', 'last_name', 'email']


# Register your models here.
admin.site.register(Teacher)
# admin.site.register(TeacherManager)
admin.site.register(GroupSpec)
admin.site.register(Group)
admin.site.register(Student, StudentAdmin)
admin.site.register(Lesson)
admin.site.register(Score_Attendance)
admin.site.register(Skill)
admin.site.register(GroupLikes)
