from django.views.generic.edit import CreateView
from .models import Partie_prenante
from .forms import PartiePrenanteForm
import matplotlib.pyplot as plt
import numpy as np
from django.http import HttpResponse
import io

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
    

def draw_radar_chart(request, points=[]):
    # Set up the radar chart
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={'projection': 'polar'})

    # Add concentric circles
    levels = [1, 2, 3, 4, 5]
    for level in levels:
        ax.plot(np.linspace(0, 2 * np.pi, 100), [level] * 100, color='gray', linewidth=0.5)

    # Add labels for each zone
    zones = ['Zone de veille', 'Zone de contrôle', 'Zone de danger']
    colors = ['green', 'orange', 'red']
    for i, level in enumerate(levels[:-1]):
        ax.fill_between(np.linspace(0, 2 * np.pi, 100), level, level + 1, color=colors[i], alpha=0.1)

    # Plot user points
    points = [(30, 2), (90, 4), (150, 3)]
    for angle, radius in points:
        ax.scatter(np.radians(angle), radius, color='blue', s=50)

    # Display labels for stakeholders (example)
    stakeholders = ['C1', 'C2', 'C3', 'F3', 'F2', 'F1']
    angles = np.linspace(0, 360, len(stakeholders), endpoint=False)
    for i, stakeholder in enumerate(stakeholders):
        ax.text(np.radians(angles[i]), 6, stakeholder, ha='center', va='center')

    # Final touches
    ax.set_ylim(0, 6)

    # Save the image to an in-memory file
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close(fig)
    buffer.seek(0)

    return HttpResponse(buffer.getvalue(), content_type="image/png")