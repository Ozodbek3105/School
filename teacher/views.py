from django.template.response import TemplateResponse

from django.shortcuts import render
from django.views import View


# Create your views here.

class AllProfessorsViewset(View):
    def get(self, request):
        return TemplateResponse(request, 'all-professors.html')


class AddProfessorViewset(View):
    def get(self, request):
        return TemplateResponse(request, "add-professor.html")


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

