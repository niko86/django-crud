from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from .filters import AttFilter
from .forms import AtterbergForm
from .models import AttModel


class AtterbergCreate(LoginRequiredMixin, CreateView):
    model = AttModel
    form_class = AtterbergForm
    template_name = 'atterberg/atterberg_form.html'
    success_url = reverse_lazy('atterberg:list')
    # LoginRequiredMixin
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'


class AtterbergUpdate(LoginRequiredMixin, UpdateView):
    model = AttModel
    form_class = AtterbergForm
    template_name = 'atterberg/atterberg_form.html'
    success_url = reverse_lazy('atterberg:list')
    # LoginRequiredMixin
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'


class AtterbergDelete(LoginRequiredMixin, DeleteView):
    model = AttModel
    success_url = reverse_lazy('atterberg:list')
    # LoginRequiredMixin
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        """Lets me delete without going to a POST confirm page"""
        return self.post(request, *args, **kwargs)


@login_required
def att_list(request):
    att_list = AttModel.objects.all()
    att_filter = AttFilter(request.GET, queryset=att_list)
    return render(request, 'core/list.html', context={'filter': att_filter})


@login_required
def download_xml(request, pk):
    att_test = get_object_or_404(AttModel, pk=pk)
    xml_data = AttModel.generate_xml(
        att_test, pretty_print=True, utf=16, definitions=True)
    response = HttpResponse(xml_data, content_type="application/xml")
    response['Content-Disposition'] = f'attachment; filename={att_test.project_id} {att_test.hole_id} {att_test.depth_top} {att_test.technician}.xml'
    return response


@login_required
def excel_xml(request):
    if request.method == "GET":
        r = request.GET

        att_test = AttModel.objects.filter(project_id=r['project_id']) \
            .filter(hole_id=r['hole_id']) \
            .filter(depth_top=r['depth_top']) \
            .filter(sample_type=r['sample_type']) \
            .first()

        xml_data = AttModel.generate_xml(
            att_test, pretty_print=False, utf=8, definitions=False)
        return HttpResponse(xml_data, content_type="application/xml")
