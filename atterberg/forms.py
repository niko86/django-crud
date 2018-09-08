from django import forms

from .models import AttModel


class AtterbergForm(forms.ModelForm):
    class Meta:
        model = AttModel
        fields = ('project_id', 'hole_id', 'depth_top', 'sample_type', 'technician', 'att_method', 'check_cal', 'check_tip', 'check_vis', 'balance', 'preparation_method', 'oven', 'oven_temp', 'sieve_total', 'sieve_retained',
                  'pl1_con', 'pl1_con_mass', 'pl1_wet_mass', 'pl1_dry1_mass', 'pl1_dry2_mass',
                  'pl2_con', 'pl2_con_mass', 'pl2_wet_mass', 'pl2_dry1_mass', 'pl2_dry2_mass',
                  'll1_pene_1', 'll1_pene_2', 'll1_pene_3', 'll1_con', 'll1_con_mass', 'll1_wet_mass', 'll1_dry1_mass', 'll1_dry2_mass',
                  'll2_pene_1', 'll2_pene_2', 'll2_pene_3', 'll2_con', 'll2_con_mass', 'll2_wet_mass', 'll2_dry1_mass', 'll2_dry2_mass',
                  'll3_pene_1', 'll3_pene_2', 'll3_pene_3', 'll3_con', 'll3_con_mass', 'll3_wet_mass', 'll3_dry1_mass', 'll3_dry2_mass',
                  'll4_pene_1', 'll4_pene_2', 'll4_pene_3', 'll4_con', 'll4_con_mass', 'll4_wet_mass', 'll4_dry1_mass', 'll4_dry2_mass',)
