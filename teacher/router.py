from django.urls import path
from rest_framework.routers import DefaultRouter

from teacher.api_view import ProfessorAPIView, ProfessorViewset, ProfessorsAPIView
router = DefaultRouter()

router.register("viewset", ProfessorViewset, "viewset")

urlpatterns = router.urls + [
    path("professors/", ProfessorsAPIView.as_view(), name="professors"),
    path("professors/professor/<int:pk>", ProfessorAPIView.as_view(), name="professor"),
]