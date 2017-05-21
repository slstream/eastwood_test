from django.views.generic import ListView
from ..models import Employee, Department

class Employees(ListView):
    model = Employee
    template_name = 'employees.html'
    context_object_name = 'employees'
    paginate_by = 3

    def get_queryset(self):
        current_department = self.request.GET.get('current_department', 'all')
        if current_department == 'all':
            return Employee.objects.all().order_by('second_name')
        else:
            return Employee.objects.filter(department__id=current_department).order_by('second_name')

    def get_context_data(self, **kwargs):
        context = super(Employees, self).get_context_data(**kwargs)

        # for filter
        context['departments'] = Department.objects.all()
        context['current_department'] = self.request.GET.get('current_department', 'all')
        return context