from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from .models import MoistureModel
from .forms import MoistureForm
from .filters import MoistureFilter


class MoistureCreate(CreateView):
    model = MoistureModel
    form_class = MoistureForm
    template_name = 'moisture/moisture_form.html'
    success_url = reverse_lazy('moisture:list') ## Change all to explicit moisture only use lab:page for templates


class MoistureUpdate(UpdateView):
    model = MoistureModel
    form_class = MoistureForm
    template_name = 'moisture/moisture_form.html'
    success_url = reverse_lazy('moisture:list')


class MoistureDelete(DeleteView):
    model = MoistureModel
    success_url = reverse_lazy('moisture:list')

    def get(self, request, *args, **kwargs):
        """Lets me delete without going to a POST confirm page"""
        return self.post(request, *args, **kwargs)


def moisture_list(request):
    moisture_list = MoistureModel.objects.all()
    moisture_filter = MoistureFilter(request.GET, queryset=moisture_list)
    return render(request, 'core/list.html', context={'filter': moisture_filter}) # list.html in project level template folder


def download_xml(request, pk):
    moisture_test = get_object_or_404(MoistureModel, pk=pk)
    xml_data = MoistureModel.generate_xml(
        moisture_test, pretty_print=True, utf=16, definitions=True)
    response = HttpResponse(xml_data, content_type="application/xml")
    response['Content-Disposition'] = f'attachment; filename={moisture_test.project_id} {moisture_test.hole_id} {moisture_test.depth_top} {moisture_test.technician}.xml'
    return response


def excel_xml(request):
    if request.method == "GET":
        r = request.GET

        moisture_test = MoistureModel.objects.filter(project_id=r['project_id']) \
            .filter(hole_id=r['hole_id']) \
            .filter(depth_top=r['depth_top']) \
            .filter(sample_type=r['sample_type']) \
            .first()

        xml_data = MoistureModel.generate_xml(
            moisture_test, pretty_print=False, utf=8, definitions=False)
        return HttpResponse(xml_data, content_type="application/xml")
