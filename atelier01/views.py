from django.shortcuts import render, get_object_or_404, redirect
from .models import Atelier01, AtelierParticipant
from .forms import Atelier01Form, AtelierParticipantForm

def atelier01_list(request):
    ateliers = Atelier01.objects.all()
    return render(request, 'atelier01_list.html', {'ateliers': ateliers})

def atelier01_detail(request, pk):
    atelier = get_object_or_404(Atelier01, pk=pk)
    return render(request, 'atelier01/atelier01_detail.html', {'atelier': atelier})

def atelier01_create(request):
    if request.method == "POST":
        form = Atelier01Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('atelier01_list')
    else:
        form = Atelier01Form()
    return render(request, 'atelier01/atelier01_form.html', {'form': form})

def atelier01_update(request, pk):
    atelier = get_object_or_404(Atelier01, pk=pk)
    if request.method == "POST":
        form = Atelier01Form(request.POST, instance=atelier)
        if form.is_valid():
            form.save()
            return redirect('atelier01_detail', pk=pk)
    else:
        form = Atelier01Form(instance=atelier)
    return render(request, 'atelier01/atelier01_form.html', {'form': form})

def atelier01_delete(request, pk):
    atelier = get_object_or_404(Atelier01, pk=pk)
    if request.method == "POST":
        atelier.delete()
        return redirect('atelier01_list')
    return render(request, 'atelier01/atelier01_confirm_delete.html', {'atelier': atelier})

def atelier_participant_create(request):
    if request.method == "POST":
        form = AtelierParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('atelier01_list')
    else:
        form = AtelierParticipantForm()
    return render(request, 'atelier01/atelier_participant_form.html', {'form': form})
