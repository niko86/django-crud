from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Row, Fieldset, Field, HTML
from crispy_forms.bootstrap import Tab, TabHolder, InlineCheckboxes

from atterberg.models import AttModel


class AtterbergForm(forms.ModelForm):
    class Meta:
        model = AttModel
        fields = ('identifier', 'att_method', 'check_cal', 'check_tip', 'check_vis', 'balance', 'preparation_method', 'oven', 'oven_temp', 'sieve_total', 'sieve_retained',
                  'll1_pene_1', 'll1_pene_2', 'll1_con', 'll1_con_mass', 'll1_wet_mass', 'll1_dry1_mass', 'll1_dry2_mass',
                  'pl1_con', 'pl1_con_mass', 'pl1_wet_mass', 'pl1_dry1_mass', 'pl1_dry2_mass',
                  'pl2_con', 'pl2_con_mass', 'pl2_wet_mass', 'pl2_dry1_mass', 'pl2_dry2_mass')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            TabHolder(
                Tab('Initial Setup',
                    'identifier', 'att_method', 'check_cal', 'check_tip', 'check_vis','balance', 'preparation_method', 'oven', 'oven_temp', 'sieve_total', 'sieve_retained'
                    ),
                Tab('Liquid Limit',
                    HTML('<div class="container"><p>Testing</p></div>'),
                    TabHolder(
                        Tab('First point', 'll1_wet_mass'),
                        Tab('Second point', 'll1_dry1_mass'),
                    )
                    ),
                Tab('Plastic Limit',
                    'pl1_con_mass',
                    Field('pl1_con_mass', css_class='form-control-sm'),
                    ),
            ),
        )
        self.helper.add_input(Submit('submit', 'Save'))
