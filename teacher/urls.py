from django.urls import path

from teacher.views import AddProfessorViewset, AllProfessorsViewset

urlpatterns = [
    path('all_professors/', AllProfessorsViewset.as_view(), name='all_professors'),
    path('add_professor/', AddProfessorViewset.as_view(), name='add_professor'),
]
