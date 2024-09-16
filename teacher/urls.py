from django.urls import path

from teacher.views import AddProfessorViewset, AllProfessorsViewset, EditProfessorViewset, ProfessorProfileViewset

urlpatterns = [
    path('all_professors/', AllProfessorsViewset.as_view(), name='all_professors'),
    path('add_professor/', AddProfessorViewset.as_view(), name='add_professor'),
    path('edit_professor/', EditProfessorViewset.as_view(), name='edit_professor'),
    path('professor_profile/', ProfessorProfileViewset.as_view(), name='professor_profile'),
]
