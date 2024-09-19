from django.urls import path

from teacher.views import AddProfessorViewset, AddStudentViewset, AllProfessorsViewset, AllStudentsViewset, DeleteProfessorViewset, EditProfessorViewset, EditStudentViewset, ProfessorProfileViewset, StudentProfileViewset

urlpatterns = [
    path('all_professors/', AllProfessorsViewset.as_view(), name='all_professors'),
    path('add_professor/', AddProfessorViewset.as_view(), name='add_professor'),
    path('edit_professor/<int:professor_id>', EditProfessorViewset.as_view(), name='edit_professor'),
    path('professor_profile/', ProfessorProfileViewset.as_view(), name='professor_profile'),
    path('delete_professor/<int:professor_id>', DeleteProfessorViewset.as_view(), name='delete_professor'),
    path('all_students/', AllStudentsViewset.as_view(), name='all_students'),
    path('add_student/', AddStudentViewset.as_view(), name='add_student'),
    path('edit_student/', EditStudentViewset.as_view(), name='edit_student'),
    path('student_profile/', StudentProfileViewset.as_view(), name='student_profile'),
]   