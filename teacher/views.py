from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.views import View

from teacher.forms import AddProfessorForm


# Create your views here.

class AllProfessorsViewset(View):
    def get(self, request):
        return TemplateResponse(request, 'all-professors.html')


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
    def get(self, request):
        return TemplateResponse(request, 'edit-professor.html')


class ProfessorProfileViewset(View):
    def get(self, request):
        return TemplateResponse(request, 'professor-profile.html')

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
