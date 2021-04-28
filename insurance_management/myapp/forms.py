from django import forms
from .models import Insurances

expiryChoices = [
    ('lifetime', 'Lifetime Valid'),
    ('pensionYear', 'Pension with yearly maturity'),
    ('pensionMonth', 'Pension with monthly maturity'),
    ('fiveYear', '5 Year Validity'),
]

insuranceChoices = [
    ('car', 'Car'),
    ('home', 'Home'),
    ('life', 'Life'),
]
confirmationChoices = [
    (True, 'Yes'),
    (False, 'No')
]
class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurances
        fields = '__all__'
        labels = {'photo':''}
        widgets = {
            'name' : forms.TextInput(),
            'policyID' : forms.Textarea(),
            'dateOfCommencement' : forms.DateInput(attrs={'type':'date'}), 
            'dateOfMaturity' : forms.DateInput(attrs={'type':'date'}),
            'expiryType' : forms.Select(choices=expiryChoices),
            'insuranceType' : forms.Select(choices=insuranceChoices), 
            'aadhar' : forms.FileInput(),
            'installmentAmount' : forms.NumberInput(),
            'maturityAmount' : forms.NumberInput(),
            'confirmation' : forms.RadioSelect(choices=confirmationChoices),
        }