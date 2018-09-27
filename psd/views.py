from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from .filters import PsdFilter
from .forms import PsdForm
from .models import PsdModel


class PsdCreate(LoginRequiredMixin, CreateView):
    model = PsdModel
    form_class = PsdForm
    template_name = 'psd/psd_form.html'
    success_url = reverse_lazy('psd:list')
    # LoginRequiredMixin
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'


class PsdUpdate(LoginRequiredMixin, UpdateView):
    model = PsdModel
    form_class = PsdForm
    template_name = 'psd/psd_form.html'
    success_url = reverse_lazy('psd:list')
    # LoginRequiredMixin
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'


class PsdDelete(LoginRequiredMixin, DeleteView):
    model = PsdModel
    success_url = reverse_lazy('psd:list')
    # LoginRequiredMixin
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        """Lets me delete without going to a POST confirm page"""
        return self.post(request, *args, **kwargs)


@login_required
def psd_list(request):
    psd_list = PsdModel.objects.all()
    psd_filter = PsdFilter(request.GET, queryset=psd_list)
    return render(request, 'core/list.html', context={'filter': psd_filter})


@login_required
def download_xml(request, pk):
    psd_test = get_object_or_404(PsdModel, pk=pk)
    xml_data = PsdModel.generate_xml(
        psd_test, pretty_print=True, utf=16, definitions=True)
    response = HttpResponse(xml_data, content_type="application/xml")
    response['Content-Disposition'] = f'attachment; filename={psd_test.project_id} {psd_test.hole_id} {psd_test.depth_top} {psd_test.technician}.xml'
    return response


@login_required
def excel_xml(request):
    if request.method == "GET":
        r = request.GET

        psd_test = PsdModel.objects.filter(project_id=r['project_id']) \
            .filter(hole_id=r['hole_id']) \
            .filter(depth_top=r['depth_top']) \
            .filter(sample_type=r['sample_type']) \
            .first()

        xml_data = PsdModel.generate_xml(
            psd_test, pretty_print=False, utf=8, definitions=False)
        return HttpResponse(xml_data, content_type="application/xml")
