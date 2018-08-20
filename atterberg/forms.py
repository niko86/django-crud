from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from atterberg.models import AttModel


class AtterbergForm(forms.ModelForm):
    class Meta:
        model = AttModel
        fields = ('att_method', 'check_cal', 'check_tip', 'check_vis', 'balance', 'preparation_method', 'oven', 'oven_temp')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
