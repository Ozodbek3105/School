from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.views import View
from django.template.response import TemplateResponse
from django.contrib.auth import authenticate, login, logout

from education.forms import AddManagerForm
from teacher.models import Group, GroupSpec, Student


@login_required(login_url='login')
def home(request):
    query_set = Student.objects.all()
    new_students = query_set.order_by('-created_at').distinct()[:7]
    total_students = query_set.count()
    courses = GroupSpec.objects.all()
    context = {
        "new_students": new_students,
        "total_students": total_students,
        "courses": courses,
    }
    return render(request, "home.html", context)

class Login(View):
    def get(self, request):
        form = AuthenticationForm()
        context = {
            'form': form
        }
        return render(request, 'page-login.html', context)
    
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():    
            email = form.cleaned_data.get("username", "")
            password = form.cleaned_data.get("password", "")
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request=request, user=user)
                return redirect("home")
        context = {
            'form': form
        }
        print(form.errors)
        return render(request, "page-login.html", context)


class AddManagerViewset(View):
    def get(self, request):
        form = AddManagerForm()
        context = {
            "form": form,
        }
        return TemplateResponse(request, "page-register.html", context)

    def post(self, request):
        form = AddManagerForm(request.POST)
        if form.is_valid():
            # user = form.save(commit=False)
            # user.is_staff = True
            # user.save()
            form.save()
            return redirect('login')
        context = {
            'form': form,
        }
        return TemplateResponse(request, "page-register.html", context)


class LogOut(View):
    def get(self, request):
        logout(request)
        return redirect("login")
    