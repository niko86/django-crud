from django import forms

from lab.models import Engineer


class EngineerForm(forms.ModelForm):
    class Meta:
        model = Engineer
        fields = ('first_name', 'last_name', 'email_address')
