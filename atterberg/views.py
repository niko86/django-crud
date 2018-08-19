from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from atterberg.models import AttModel
from atterberg.forms import AtterbergForm

# Create your views here.
class IndexView(View):

    def get(self, request):
        return render(request, 'atterberg/index.html')

# Atterberg Views

class AtterbergCreate(CreateView):
    model = AttModel
    form_class = AtterbergForm
    template_name = 'atterberg/atterberg_form.html'
    success_url = reverse_lazy('atterberg:atterberg-list')

class AtterbergUpdate(UpdateView):
    model = AttModel
    form_class = AtterbergForm
    template_name = 'atterberg/atterberg_form.html'
    success_url = reverse_lazy('atterberg:atterberg-list')

class AtterbergDelete(DeleteView):
    model = AttModel
    success_url = reverse_lazy('atterberg:atterberg-list')

    def get(self, request, *args, **kwargs):
        """Lets me delete without going to a POST confirm page"""
        return self.post(request, *args, **kwargs)

class AtterbergList(ListView):
    model = AttModel
    template_name = 'atterberg/atterberg_list.html'
    context_object_name = 'atterbergs'

#class AtterbergDetail(DetailView):
#    model = AttModel