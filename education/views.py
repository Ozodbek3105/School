from django.shortcuts import render

from teacher.models import Group, GroupSpec, Student


def home(request):
    query_set = Student.objects.all()
    new_students =query_set.order_by('-created_at')[:7]
    total_students = query_set.count()
    courses = GroupSpec.objects.all()
    context = {
        "new_students": new_students,
        "total_students": total_students,
        "courses": courses,
    }
    return render(request, "home.html", context)
