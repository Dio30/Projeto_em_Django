from django.shortcuts import render,redirect, get_object_or_404
from .models import Person
from .forms import PessonForm
from django.contrib.auth.decorators import login_required

@login_required
def persons_list(request):
    persons = Person.objects.all()
    return render(request, 'pessoa.html', {'persons': persons})

@login_required
def persons_new(request):
    form = PessonForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})

@login_required
def persons_update(request,id):
    person = get_object_or_404(Person, pk=id)
    form = PessonForm(request.POST or None, request.FILES or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})

@login_required
def persons_delete(request,id):
    person = get_object_or_404(Person, pk=id)
    if request.method == 'POST':
        person.delete()
        return redirect('person_list')
    return render(request, 'person_delete.html', {'person': person})
