from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.views import View

from login.forms import AddManagerForm



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
