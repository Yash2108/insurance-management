from django import forms
from .models import Insurances

expiryChoices = [
    ('lifetime', 'Lifetime Valid'),
    ('pensionYear', 'Pension with yearly maturity'),
    ('pensionMonth', 'Pension with monthly maturity'),
    ('fiveYear', '5 Year Validity')]
insuranceChoices = [
    ('car', 'Car'),
    ('home', 'Home'),
    ('life', 'Life')]
confirmationChoices = [
    (True, 'Yes'),
    (False, 'No')]

class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurances
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'required':True}),
            'policyID' : forms.NumberInput(),
            'dateOfCommencement' : forms.DateInput(
                attrs={
                    'type':'date',
                    'required':True, 
                    'placeholder':'Pick a date'
                    }),
            'dateOfMaturity' : forms.DateInput(format=('%Y-%m-%d'),attrs={'type':'date', 'required':True}),
            'expiryType' : forms.Select(choices=expiryChoices, attrs={'required':True}),
            'insuranceType' : forms.RadioSelect(choices=insuranceChoices), 
            'aadhar' : forms.FileInput(attrs={'required':True}),
            'installmentAmount' : forms.NumberInput(attrs={'required':True}),
            'maturityAmount' : forms.NumberInput(attrs={'required':True}),
            'confirmation' : forms.CheckboxInput( attrs={'required':True}),
            'comments': forms.Textarea(attrs={'style': 'height: 60px;width:150px;'})
        }