from django import forms

from .models import MoistureModel


class MoistureForm(forms.ModelForm):
    class Meta:
        model = MoistureModel
        fields = ('project_id',)
