from django.contrib import admin

from teacher.models import Group, GroupSpec, Lesson, Score_Attendance, Student, Teacher, TeacherManager

# Register your models here.
admin.site.register(Teacher)
# admin.site.register(TeacherManager)
admin.site.register(GroupSpec)
admin.site.register(Group)
admin.site.register(Student)
admin.site.register(Lesson)
admin.site.register(Score_Attendance)

