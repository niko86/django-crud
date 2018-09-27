from django import forms

from .models import PsdModel


class PsdForm(forms.ModelForm):
    class Meta:
        model = PsdModel
        fields = ('project_id',
                  'hole_id',
                  'depth_top',
                  'sample_type',
                  'technician',
                  'check_cal',
                  'check_vis',
                  'test_method',
                  
                  'container_id',
                  'container_mass',
                  'initial_wet_mass',
                  'initial_dry_mass',
                  'accepted_dry_mass',
                  'description',
                  'natural_condition',
                  'dried_condition',

                  'mass_125mm',
                  'mass_90mm',
                  'mass_75mm',
                  'mass_63mm',
                  'mass_50mm',
                  'mass_37p5mm',
                  'mass_28mm',
                  'mass_20mm',
                  'mass_below_20mm',
                  'sum_stack_1',
                  'riffle_mass_below_20mm',
                  'dry_washed_mass',

                  'mass_14mm',
                  'mass_10mm',
                  'mass_6p3mm',
                  'mass_below_6p3mm',
                  'sum_stack_2',
                  'riffle_mass_below_6p3mm',

                  'mass_5mm',
                  'mass_3p35mm',
                  'mass_2mm',
                  'mass_1p18mm',
                  'mass_600um',
                  'mass_425um',
                  'mass_300um',
                  'mass_212um',
                  'mass_150um',
                  'mass_63um',
                  'sum_stack_3',
                  'remarks',
                  )
