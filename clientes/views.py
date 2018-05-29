from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Person
from .forms import PersonForm

@login_required
def persons_list(request):
	persons = Person.objects.all()
	return render(request, 'index.html',{'persons': persons})

@login_required
def persons_new(request):
	# se preenchido, ele carrega preenchido, senao vazio
	form = PersonForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('persons_list')
	return render(request, 'person_form.html',{'form':form})

@login_required
def persons_update(request, id):
	person = get_object_or_404(Person, pk=id)
	form = PersonForm(request.POST or None, request.FILES or None, instance=person)

	if form.is_valid():
		form.save()
		return redirect('persons_list')
	return render(request, 'person_form.html', {'form':form})

@login_required
def persons_delete(request, id):
	person = get_object_or_404(Person, pk=id)
	form = PersonForm(request.POST or None, request.FILES or None, instance=person)

	if request.method == 'POST':
		person.delete()
		return redirect('persons_list')
	return render(request, 'person_delete_confirm.html', {'form':form, 'person':person.first_name})	