from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.views import View
from django.contrib.auth.forms import  AuthenticationForm
from login.forms import AddManagerForm
from django.contrib import auth


# Create your views here.


class AddManagerViewset(View):
    def get(self, request):
        form = AddManagerForm()
        context = {
            "form": form,
        }
        return TemplateResponse(request, "registration.html", context)

    def post(self, request):
        form = AddManagerForm(request.POST)
        if form.is_valid():
            # user = form.save(commit=False)
            # user.is_staff = True
            # user.save()
            form.save()
            return redirect('home')
        context = {
            'form': form,
        }
        return TemplateResponse(request, "registration.html", context)


class AuthenticateProfessor(View):
    def get(self,request):
        form = AuthenticationForm()
        context = {
            "form": form,  
        }
        return TemplateResponse(request,'page-login.html',context)
    def post(self,request):
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = auth.authenticate(email=email,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('home')
        context = {
            'form': form,
        }
        return TemplateResponse(request,'page-login.html',context)
    

class LogoutProfessor(View):
    def get( self,request): 
        auth.logout(request)
        return redirect('auth_professor')