from django_filters import CharFilter, FilterSet

from .models import AttModel

class AttFilter(FilterSet):
    project_id = CharFilter(lookup_expr='icontains')
    hole_id = CharFilter(lookup_expr='icontains')

    class Meta:
        model = AttModel
        fields = [
            'project_id',
            'hole_id',
            'depth_top',
            ]
