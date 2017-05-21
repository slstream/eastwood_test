from django.views.generic import DetailView
from ..models import Employee

class Employee(DetailView):
    model = Employee
    template_name = 'employee.html'
    context_object_name = 'employee'
