from django import forms
from .models import Insurances

class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurances
        fields = '__all__'
        labels = {'photo':''}