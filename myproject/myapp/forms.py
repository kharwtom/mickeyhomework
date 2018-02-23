from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.admin import widgets
from .models import Person
from .models import Rent

class PersonForm(ModelForm):
	class Meta:
		model =  Person
		exclude=[]

	
		
	def __init__(self, *args, **kwargs):
		super(PersonForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit'))

class RentForm(ModelForm):
	class Meta:
		model =  Rent
		exclude=['user','stop']
		
	
		
	def __init__(self, *args, **kwargs):
		super(RentForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit'))