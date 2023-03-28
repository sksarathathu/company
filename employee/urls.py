from django.urls import path
from employee import views


urlpatterns = [
    path("",views.EmployeeRegisterView.as_view(),name="register"),
    path("list",views.EmployeeListView.as_view(),name="listemp"),
    path("delete/<int:id>",views.EmployeeDeleteView.as_view(),name="delete"),
    path("update/<int:id>",views.EmployeeUpdateView.as_view(),name="empupdate")
    
]