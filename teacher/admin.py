from django import forms
from django.contrib import admin
from django.contrib.auth.hashers import make_password

from teacher.models import Group, GroupLikes, GroupSpec, Lesson, LessonFiles, Score_Attendance, Skill, Student, Teacher, TeacherManager

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
    ordering = ("id", "first_name", "last_name")
    sortable_by = ("gender",)
    list_display_links = ['id', 'first_name', 'last_name', 'email']


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"

        widgets = {
            'skills': forms.CheckboxSelectMultiple
        }


class TeacherAdmin(admin.ModelAdmin):
    form = TeacherForm
    list_display = ["id", "first_name", "last_name", 'email', 'phone']
    list_display_links = ("id", "first_name", "last_name")

    def save_model(self, request, obj, form, change):
        # print(obj.groups.all())
        obj.password = make_password(obj.password)
        # obj.save()
        # if 'skills' in form.cleaned_data:
        #     obj.skills.set(form.cleaned_data['skills'])
        return super().save_model(request, obj, form, change)


class LessonFilesAdmin(admin.ModelAdmin):
    list_display = ["id", "file", "lesson"]


class Score_AttendanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'lesson', 'mark', 'is_present']


# Register your models here.
admin.site.register(Teacher, TeacherAdmin)
# admin.site.register(TeacherManager)
admin.site.register(GroupSpec)
admin.site.register(Group)
admin.site.register(Student, StudentAdmin)
admin.site.register(Lesson)
admin.site.register(Score_Attendance, Score_AttendanceAdmin)
admin.site.register(Skill)
admin.site.register(GroupLikes)
admin.site.register(LessonFiles, LessonFilesAdmin)
