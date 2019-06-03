from django import forms
from .models import pages

class SearchForm(forms.ModelForm):
	"""Formulario para realizar busquedas"""
	class Meta:
		model = pages
		fields = ('titulo',)
			
		