from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
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

def download_xml(request, pk):
    att_test = get_object_or_404(AttModel, pk=pk)
    xml_data = AttModel.generate_xml(att_test) # Have to force object into dictionary
    response = HttpResponse(xml_data, content_type="application/xml")
    response['Content-Disposition'] = f'attachment; filename={att_test.identifier}.xml'
    return response
    #return HttpResponse(xml_data, content_type="application/xml")