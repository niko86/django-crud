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
    success_url = reverse_lazy('atterberg:list')

class AtterbergUpdate(UpdateView):
    model = AttModel
    form_class = AtterbergForm
    template_name = 'atterberg/atterberg_form.html'
    success_url = reverse_lazy('atterberg:list')

class AtterbergDelete(DeleteView):
    model = AttModel
    success_url = reverse_lazy('atterberg:list')

    def get(self, request, *args, **kwargs):
        """Lets me delete without going to a POST confirm page"""
        return self.post(request, *args, **kwargs)

class AtterbergList(ListView):
    model = AttModel
    template_name = 'atterberg/atterberg_list.html'
    context_object_name = 'atterbergs'

def download_xml(request, pk):
    att_test = get_object_or_404(AttModel, pk=pk)
    xml_data = AttModel.generate_xml(att_test, pretty_print=True, utf=16, definitions=True)
    response = HttpResponse(xml_data, content_type="application/xml")
    response['Content-Disposition'] = f'attachment; filename={att_test.project_id} {att_test.hole_id} {att_test.depth_top} {att_test.technician}.xml'
    return response

def excel_xml(request):
    if request.method == "GET":
        r = request.GET

        att_test = AttModel.objects.filter(project_id=r['project_id']) \
            .filter(hole_id=r['hole_id']) \
            .filter(depth_top=r['depth_top']) \
            .filter(sample_type=r['sample_type']) \
            .first()

        xml_data = AttModel.generate_xml(att_test, pretty_print=False, utf=8, definitions=False)
        return HttpResponse(xml_data, content_type="application/xml")
