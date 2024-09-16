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
    