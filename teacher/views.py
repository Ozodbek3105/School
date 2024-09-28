import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views import View

from teacher.forms import AddCourseForm, AddLessonForm, AddProfessorForm, EditLessonForm, EditProfessorForm, \
    AddStudentForm, EditStudentForm, StudentsAttendanceFormSet
from teacher.models import Group, Lesson, LessonFiles, Score_Attendance, Student

# Create your views here.


User = get_user_model()


class AllProfessorsViewset(LoginRequiredMixin, View):
    login_url = "login"

    def get(self, request):
        teachers = User.objects.all()
        context = {"teachers": teachers}
        return TemplateResponse(request, 'all-professors.html', context)


class AddProfessorViewset(LoginRequiredMixin, PermissionRequiredMixin, View):
    login_url = 'login'
    permission_required = 'teacher.add_teacher'
    
    def get(self, request):
        form = AddProfessorForm()
        context = {
            'form': form,
        }
        return TemplateResponse(request, "add-professor.html", context)
    
    def post(self, request):
        form = AddProfessorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("all_professors")
        context = {'form': form}
        print(form.errors)
        print(form.data)
        return TemplateResponse(request, "add-professor.html", context)


class EditProfessorViewset(LoginRequiredMixin, PermissionRequiredMixin, View):
    login_url = 'login'
    permission_required = 'teacher.change_teacher'

    def get(self, request, professor_id):
        teacher = get_object_or_404(User, id=professor_id)
        form = AddProfessorForm(instance=teacher)
        context = {
            'form': form,
            "teacher": teacher,
        }
        print(form.as_p())
        print('caafaw ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd  ')
        return TemplateResponse(request, 'edit-professor.html', context)
    
    def post(self, request, professor_id):
        teacher = get_object_or_404(User, id=professor_id)
        form = EditProfessorForm(request.POST, request.FILES, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('all_professors')
        context = {
            'form': form,
            'teacher': teacher,
        }
        print(form.errors)
        return TemplateResponse(request, "edit-professor.html", context)


class ProfessorProfileViewset(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request, professor_id):
        professor = get_object_or_404(User, id=professor_id)
        context = {
            'professor': professor,
        }
        return TemplateResponse(request, 'professor-profile.html', context)


class DeleteProfessorViewset(PermissionRequiredMixin, LoginRequiredMixin, View):
    login_url = 'login'
    permission_required = ["teacher.delete_teacher"]

    def get(self, request, professor_id=None):
        if professor_id:
            teacher = get_object_or_404(User, id=professor_id)
            teacher.delete()
            professor_id += 1
            return HttpResponseRedirect(request.META.get("HTTP_REFERER", ""))
            # return HttpResponseRedirect(request.path_info) # Does not work properly


class AllStudentsViewset(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request):
        students = Student.objects.all()
        context = {
            "students": students,
        }
        return TemplateResponse(request, 'all-students.html',context)


class AddStudentViewset(LoginRequiredMixin, PermissionRequiredMixin, View):
    login_url = 'login'
    permission_required = 'teacher.add_student'

    def get(self, request):
        form = AddStudentForm()
        context = {
            'form': form,
        }
        return TemplateResponse(request, "add-student.html",context)

    def post(self, request,):
        form = AddStudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("all_students")
        context = {'form': form}
        print(form.errors)
        return TemplateResponse(request, "add-student.html", context)
    

class EditStudentViewset(LoginRequiredMixin, PermissionRequiredMixin, View):
    login_url = 'login'
    permission_required = 'teacher.change_student'

    def get(self, request,student_id):
        student = get_object_or_404(Student, id=student_id)
        form = EditStudentForm(instance=student)
        context = {
            "form":form,
            "student":student,
        }
        return TemplateResponse(request, 'edit-student.html',context)

    def post(self,request,student_id):
        student = get_object_or_404(Student, id=student_id)
        form = EditStudentForm(request.POST,request.FILES,instance=student)
        if form.is_valid():
            form.save()
            return redirect('all_students')
        context = {
            "form": form,
            "student":student,
        }
        print("errrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr",form.errors)
        return TemplateResponse(request, 'edit-student.html',context)
    

class DeleteStudentViewset(LoginRequiredMixin, PermissionRequiredMixin, View):
    login_url = 'login'
    permission_required = 'teacher.delete_student'

    def post(self, request, student_id):
        student = Student.objects.get(id=student_id)
        student.delete()
        return redirect("all_students")


class StudentProfileViewset(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request, student_id):
        return TemplateResponse(request, 'about-student.html')


class AllCoursesViewset(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request):
        courses = Group.objects.all()
        context = {
            "courses": courses
            }
        return TemplateResponse(request, 'all-courses.html', context)


class AddCoursesViewset(LoginRequiredMixin, PermissionRequiredMixin, View):
    login_url = 'login'
    permission_required = 'teacher.add_course'

    def get(self, request):
        form = AddCourseForm()
        context = {
            "form": form
            }
        return TemplateResponse(request, 'add-courses.html', context)
    
    def post(self, request):
        form = AddCourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("all_courses")
        context = {
            'form': form
        }
        print(form.errors)
        print(form.data)
        return TemplateResponse(request, "add-courses.html", context)
        

class EditCoursesViewset(LoginRequiredMixin, PermissionRequiredMixin, View):
    login_url = 'login'
    permission_required = 'teacher.edit_course'

    def get(self, request, course_id):
        course = get_object_or_404(Group, id=course_id)
        form = AddCourseForm(instance=course)
        context = {
            'form': form,
            'course': course
        }
        return TemplateResponse(request, 'edit-courses.html', context)
    
    def post(self, request, course_id):
        course = get_object_or_404(Group, id=course_id)
        form = AddCourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('all_courses')
        context = {
            'form': form,
            'course': course
        }
        print(form.errors)
        print(form.data)
        return TemplateResponse(request, 'edit-courses.html', context)


class DeleteCoursesViewset(LoginRequiredMixin, PermissionRequiredMixin, View):
    login_url = 'login'
    permission_required = 'teacher.delete_course'

    def get(self, request, course_id):
        course = get_object_or_404(Group, id=course_id)
        course.delete()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER", ""))


class AllLessonsViewset(LoginRequiredMixin, PermissionRequiredMixin, View):
    login_url = 'login'
    permission_required = ''
    def get(self, request):
        lessons = Lesson.objects.all()
        context = {
            'lessons': lessons
        }
        return TemplateResponse(request, 'all-lessons.html', context)
    

class AddLessonViewset(LoginRequiredMixin, PermissionRequiredMixin, View):
    login_url = 'login'
    permission_required = 'teacher.add_lesson'

    def get(self, request):
        form = AddLessonForm()
        context = {
            'form': form
        }
        return TemplateResponse(request, 'add-lesson.html', context)

    def post(self, request):
        form = AddLessonForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            files = request.FILES.getlist("files", None)
            if files:
                for file in files:
                    LessonFiles.objects.create(
                        file=file,
                        lesson=lesson
                    )
            return redirect('all_lessons')

        context = {
            "form": form
        }
        return TemplateResponse(request, 'add-lesson.html', context)


class EditLessonViewset(PermissionRequiredMixin, LoginRequiredMixin, View):
    login_url = 'login'
    permission_required = ''

    def get(self, request, lesson_id):
        lesson = Lesson.objects.get(id=lesson_id)
        files = LessonFiles.objects.filter(lesson=lesson)
        form = EditLessonForm(instance=lesson)
        print('--------------------------------------------')
        print(files)
        print('--------------------------------------------')
        context = {
            'form': form,
            'files': files,
            'lesson': lesson,
        }
        return TemplateResponse(request, 'edit-lesson.html', context)

    def post(self, request, lesson_id):
        lesson = Lesson.objects.get(id=lesson_id)
        form = EditLessonForm(request.POST, instance=lesson)
        if form.is_valid():
            lesson = form.save()
            # old_files = LessonFiles.objects.filter(lesson=lesson)
            # old_files.delete()
            files = request.FILES.getlist('files', None)
            if files:
                for file in files:
                    LessonFiles.objects.create(
                        lesson=lesson,
                        file=file,
                    )
            return redirect('all_lessons')
        files = LessonFiles.objects.filter(lesson=lesson)
        context = {
            "form": form,
            'files': files,
            'lesson': lesson,
        }
        return TemplateResponse(request, 'edit-lesson.html', context)


def delete_lesson_file(request, lesson_file_id):
    print("+++++++++++++++++++++++++++++++++++++++++++")
    lesson_file = get_object_or_404(LessonFiles, id=lesson_file_id)
    lesson_id = lesson_file.lesson.id
    lesson_file.delete()
    return redirect("edit_lesson", lesson_id=lesson_id)


class AboutCoursesViewset(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request, course_id):
        course = get_object_or_404(Group, id=course_id)
        context = {
            course: course
        }
        return TemplateResponse(request, 'about-courses.html', context)


class ViewCoursesViewset(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request, course_id):
        course = Group.objects.get(id=course_id)
        lessons = Lesson.objects.filter(group=course)
        context = {
            'lessons': lessons
        }
        return TemplateResponse(request, "view-lessons.html", context)
    

class Attendance(LoginRequiredMixin, View):
    # permission_required = 'teacher.change_score_attendance'
    login_url = "login"
    def get(self, request, lesson_id):
        print('88888888888888888888888888888888888888888888888888')
        print(request.user.get_all_permissions())
        print('88888888888888888888888888888888888888888888888888')
        lesson = Lesson.objects.get(id=lesson_id)
        group = lesson.group
        students = group.student_set.all()
        print(students)
        print(lesson.score_attendance_set.filter(lesson=lesson, student__in=students))
        print('88888888888888888888888888888888888888888888888888')
        
        # if not lesson.score_attendance_set.filter(lesson=lesson, student__in=students):
        Score_Attendance.objects.bulk_create(
            Score_Attendance(lesson=lesson, student=student) for student in students
            if not Score_Attendance.objects.filter(lesson=lesson, student=student).exists()
        )
        # formset = StudentsAttendanceFormSet(queryset=Score_Attendance.objects.filter(
        #     created_at__exact=datetime.date.today())
        # )
        # for att in Score_Attendance.objects.filter(lesson)
        formset = StudentsAttendanceFormSet(queryset=lesson.score_attendance_set.filter(lesson=lesson, student__in=students))
        print(lesson.score_attendance_set.filter(lesson=lesson, student__in=students))
        context = {
            'formset': formset,
            'lesson': lesson,
            'group': group
        }
        return TemplateResponse(request, "yoqlama.html", context)

    def post(self, request, lesson_id):
        lesson = Lesson.objects.get(id=lesson_id)
        queryset = Score_Attendance.objects.filter(created_at__exact=datetime.date.today())
        formset = StudentsAttendanceFormSet(request.POST, queryset=queryset)
        group = lesson.group
        students = group.student_set.all()
        if formset.is_valid():
            print("//////////////////////////////////////////////")
            print(formset)
            print("//////////////////////////////////////////////")
            instances = formset.save(commit=False)

            for form, student in zip(instances, students):
                form.lesson = lesson
                form.student = student
                form.save()

            return redirect('view_course', group.id)
        
        for form, student in zip(formset.forms, students):
            form.instance.student = student

        context = {
            'formset': formset,
            'lesson': lesson,
            'group': group
        }
        print(queryset)
        # print(formset)
        print(formset.errors)
        return TemplateResponse(request, 'yoqlama.html', context)
    