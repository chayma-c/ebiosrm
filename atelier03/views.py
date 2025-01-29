from django.views.generic.edit import CreateView
from .models import Partie_prenante
from .forms import PartiePrenanteForm

class PartiePrenanteCreateView(CreateView):
    model = Partie_prenante
    form_class = PartiePrenanteForm
    template_name = 'your_form_template.html'
    success_template = 'success.html'  # Create this template

    def form_valid(self, form):
        # Save the form first to get the instance
        response = super().form_valid(form)
        
        # Calculate criticality after saving
        self.object.refresh_from_db()  # Ensure fresh data
        criticality = self.object.current_criticality
        
        # Add to template context
        context = self.get_context_data(criticality=criticality)
        return self.render_to_response(context)
    
    # views.py
from django.views.generic.edit import FormView

class PartiePrenanteFormView(FormView):
    template_name = 'form_with_result.html'
    form_class = PartiePrenanteForm
    success_url = '/success/'  # Or same page

    def form_valid(self, form):
        instance = form.save()
        criticality = instance.current_criticality
        return self.render_to_response(
            self.get_context_data(
                form=form,
                criticality=criticality
            )
        )