from django_filters import CharFilter, FilterSet

from .models import PsdModel

class PsdFilter(FilterSet):
    project_id = CharFilter(lookup_expr='icontains')
    hole_id = CharFilter(lookup_expr='icontains')

    class Meta:
        model = PsdModel
        fields = [
            'project_id',
            'hole_id',
            'depth_top',
            ]
