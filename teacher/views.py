from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.views import View

from teacher.forms import AddCourseForm, AddProfessorForm, EditProfessorForm

from django.contrib.auth import get_user_model

from teacher.models import Group

# Create your views here.


User = get_user_model()


class AllProfessorsViewset(View):
    def get(self, request):
        teachers = User.objects.all()
        context = {"teachers": teachers}
        return TemplateResponse(request, 'all-professors.html', context)


class AddProfessorViewset(View):
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


class EditProfessorViewset(View):
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


class ProfessorProfileViewset(View):
    def get(self, request):
        return TemplateResponse(request, 'professor-profile.html')


class DeleteProfessorViewset(View):
    def get(self, request, professor_id=None):
        if professor_id:
            teacher = get_object_or_404(User, id=professor_id)
            teacher.delete()
            professor_id += 1
            return HttpResponseRedirect(request.META.get("HTTP_REFERER", ""))
            # return HttpResponseRedirect(request.path_info) # Does not work properly


class AllStudentsViewset(View):
    def get(self, request):
        return TemplateResponse(request, 'all-students.html')


class AddStudentViewset(View):
    def get(self, request):
        return TemplateResponse(request, "add-student.html")


class EditStudentViewset(View):
    def get(self, request):
        return TemplateResponse(request, 'edit-student.html')


class StudentProfileViewset(View):
    def get(self, request):
        return TemplateResponse(request, 'about-student.html')


class AllCoursesViewset(View):
    def get(self, request):
        courses = Group.objects.all()
        context = {
            "courses": courses
            }
        return TemplateResponse(request, 'all-courses.html', context)


class AddCoursesViewset(View):
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
        

class EditCoursesViewset(View):
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


class DeleteCoursesViewset(View):
    def get(self, request, course_id):
        course = get_object_or_404(Group, id=course_id)
        course.delete()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER", ""))


class AboutCoursesViewset(View):
    def get(self, request):
        return TemplateResponse(request, 'about-courses.html')

