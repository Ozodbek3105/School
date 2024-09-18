from django.contrib import admin

from teacher.models import Group, GroupSpec, Lesson, Score_Attendance, Student, Teacher, TeacherManager


class TeacherAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "email", "phone", "gender", "department")
    ordering = ('id', "first_name", "last_name", "email")
    list_display_links = ("id", "first_name",)
    list_editable = ("gender", "department")


# Register your models here.
admin.site.register(Teacher, TeacherAdmin)
# admin.site.register(TeacherManager)
admin.site.register(GroupSpec)
admin.site.register(Group)
admin.site.register(Student)
admin.site.register(Lesson)
admin.site.register(Score_Attendance)

