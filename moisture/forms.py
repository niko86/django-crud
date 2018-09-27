from django import forms

from .models import MoistureModel


class MoistureForm(forms.ModelForm):
    class Meta:
        model = MoistureModel
        fields = ('project_id','hole_id', 'depth_top', 'sample_type', 'mc_method', 'technician', 'balance', 'oven', 'oven_temp',
        'mc_con', 'mc_con_mass', 'mc_wet_mass', 'mc_dry1_mass', 'mc_dry2_mass',
        )
