from django.shortcuts import render

# Create your views here.

from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .forms import PersonForm
from .forms import RentForm
from .models import Person
from .models import Rent
from .models import Car

from django.shortcuts import render

def home(request):
	return render(request, 'home.html', {'key': "value" })

class CreatePersonView(CreateView):
	queryset = Person()
	template_name='create.html'
	form_class = PersonForm
	success_url = '/admin'

class ListPersonView(ListView):
    model = Person
    template_name='list.html'

class CreateRentView(CreateView):
	queryset = Rent()
	template_name='create.html'
	form_class = RentForm
	success_url = '/home'

	def form_valid(self,form):
		form.instance.user = self.request.user
		return super(CreateRentView,self).form_valid(form)
	
class ListModelView(ListView):
	model = Car
	template_name='model.html'