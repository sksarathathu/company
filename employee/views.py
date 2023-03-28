from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employees
from django.views.generic import CreateView,ListView,View,FormView
from django.contrib import messages
from django.urls import reverse_lazy


class EmployeeRegisterView(CreateView):
    template_name="register.html"
    form_class=EmployeeForm
    success_url=reverse_lazy("listemp")

    def form_valid(self, form):
        messages.success(self.request,"Registered successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"Registration failed ")
        return super().form_invalid(form)

class EmployeeListView(ListView):
    template_name="emplist.html"
    model=Employees
    context_object_name="employee"

class EmployeeDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Employees.objects.get(id=id).delete()
        messages.success(self.request,"Deleted successfully")
        return redirect('listemp')

class EmployeeUpdateView(FormView):
    template_name="empupdate.html"
    form_class=EmployeeForm

    def post(self,request,*args,**kwargs):
        id=kwargs.get("id")
        name=request.POST.get("name")
        email=request.POST.get("email")
        contact=request.POST.get("contact")
        Employees.objects.filter(id=id).update(name=name,email=email,contact=contact)
        messages.success(self.request,"Updated successfully")
        return redirect("listemp")
        

