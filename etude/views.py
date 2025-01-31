from django.shortcuts import render, get_object_or_404, redirect
from .models import Etude
from .forms import EtudeForm

def test(request):
    return render(request, 'test.html', {})

def etude_list(request):
    """View to list all studies, handle study creation, and enable searching."""
    
    query = request.GET.get('q', '')  # Get search query from request
    etudes = Etude.objects.all()  # Fetch all studies

    if query:
        etudes = etudes.filter(nom__icontains=query)  # Filter studies by name

    if request.method == "POST":
        form = EtudeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('etude_list')  # Redirect to refresh the list

    else:
        form = EtudeForm()

    return render(request, 'etude_list.html', {'etudes': etudes, 'form': form, 'query': query})

def etude_detail(request, etude_id):
    """View to display study details and link to edit workshops."""
    etude = get_object_or_404(Etude, id=etude_id)
    return render(request, 'etude_detail.html', {'etude': etude})
