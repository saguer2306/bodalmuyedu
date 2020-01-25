from django.shortcuts import render, redirect

from django.urls import reverse

from .forms import PersonaForm

from .models import Persona
# Create your views here.

def guardar_invitado(request):
	form = PersonaForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('wed:confirmar')

	return render(request, 'app_wed/inicio_app.html', {'form':form})