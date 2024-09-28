from django.urls import path

from teacher.views import *

urlpatterns = [
    path('all_professors/', AllProfessorsViewset.as_view(), name='all_professors'),
    path('add_professor/', AddProfessorViewset.as_view(), name='add_professor'),
    path('edit_professor/<int:professor_id>', EditProfessorViewset.as_view(), name='edit_professor'),
    path('professor_profile/<int:professor_id>', ProfessorProfileViewset.as_view(), name='professor_profile'),
    path('delete_professor/<int:professor_id>', DeleteProfessorViewset.as_view(), name='delete_professor'),
    path('all_students/', AllStudentsViewset.as_view(), name='all_students'),
    path('add_student/', AddStudentViewset.as_view(), name='add_student'),
    path('edit_student/<int:student_id>', EditStudentViewset.as_view(), name='edit_student'),
    path('delete_student/<int:student_id>', DeleteStudentViewset.as_view(), name='delete_student'),
    path('student_profile/<int:student_id>', StudentProfileViewset.as_view(), name='student_profile'),
    path('all_courses/', AllCoursesViewset.as_view(), name='all_courses'),
    path('add_course/', AddCoursesViewset.as_view(), name='add_course'),
    path('edit_course/<int:course_id>', EditCoursesViewset.as_view(), name='edit_course'),
    path('about_course/<int:course_id>', AboutCoursesViewset.as_view(), name='about_course'),
    path('delete_course/<int:course_id>', DeleteCoursesViewset.as_view(), name='delete_course'),
    path('view_course/<int:course_id>', ViewCoursesViewset.as_view(), name='view_course'),
    path('add_leesson/', AddLessonViewset.as_view(), name='add_lesson'),
    path('all_lessons/', AllLessonsViewset.as_view(), name='all_lessons'),
    path('edit_lesson/<int:lesson_id>', EditLessonViewset.as_view(), name='edit_lesson'),
    path('delete_lesson_file/<int:lesson_file_id>/', delete_lesson_file, name='delete_lesson_file'),
    path('attendance/<int:lesson_id>', Attendance.as_view(), name='attendance')
]
