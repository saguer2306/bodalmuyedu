from django import forms

from .models import Persona


class PersonaForm(forms.ModelForm):
	class Meta:
		model = Persona
		fields = "__all__"

	def __init__(self, *args, **kwargs):
		super(PersonaForm, self).__init__(*args, **kwargs)
		self.fields['nombre'].widget.attrs['class'] = 'w3-input w3-border w3-round'
		self.fields['intolerancia'].widget.attrs['class'] = 'w3-select w3-border w3-round'
		self.fields['transporte'].widget.attrs['class'] = 'w3-check'