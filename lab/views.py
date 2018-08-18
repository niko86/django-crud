from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from lab.models import Engineer
from lab.forms import EngineerForm

# Create your views here.
class IndexView(View):

    def get(self, request):
        return render(request, 'lab/index.html', {'message': 'Hello World'})

# Engineer Views

class EngineerCreate(CreateView):
    model = Engineer
    form_class = EngineerForm
    template_name = 'lab/engineer_form.html'
    success_url = reverse_lazy('lab:engineer-list')

class EngineerUpdate(UpdateView):
    model = Engineer
    form_class = EngineerForm
    template_name = 'lab/engineer_form.html'
    success_url = reverse_lazy('lab:engineer-list')

class EngineerDelete(DeleteView):
    model = Engineer
    success_url = reverse_lazy('lab:engineer-list')

    def get(self, request, *args, **kwargs):
        """Lets me delete without going to a POST confirm page"""
        return self.post(request, *args, **kwargs)

class EngineerList(ListView):
    model = Engineer
    template_name = 'lab/engineer_list.html'
    context_object_name = 'engineers'

class EngineerDetail(DetailView):
    model = Engineer

# Project Views

