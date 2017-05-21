from django.views.generic import TemplateView
from ..models import Employee

class AlphabeticalNotesView(TemplateView):
    template_name = "alpha_notes.html"

    def get_context_data(self, kwargs):
        context = super(AlphabeticalNotesView, self).get_context_data(kwargs)
        context['data'] = Employee.objects.all()
        return context
