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
        labels = {
            'name' : 'Name',
            'policyID' : 'Policy ID',
            'dateOfCommencement' : 'Date of Commencement', 
            'dateOfMaturity' : 'Date of Maturity',
            'expiryType' : 'Expirty Type',
            'insuranceType' : 'Insurance Type', 
            'aadhar' : 'Upload Aadhar Card Photo',
            'installmentAmount' : 'Installment Amount',
            'maturityAmount' : 'Maturity Amount',
            'confirmation' : 'Are you sure you want to upload this?',
            }

        widgets = {
            'name' : forms.TextInput(attrs={'required':True}),
            'policyID' : forms.Textarea(attrs={'style': 'height: 30px;width:150px;', 'required':True}),
            'dateOfCommencement' : forms.DateInput(
                attrs={
                    'type':'date',
                    'required':True, 
                    'placeholder':'Pick a date'
                    }),
            'dateOfMaturity' : forms.DateInput(format=('%Y-%m-%d'),attrs={'type':'date', 'required':True}),
            'expiryType' : forms.Select(choices=expiryChoices, attrs={'required':True}),
            'insuranceType' : forms.CheckboxSelectMultiple(choices=insuranceChoices, attrs={'required':True}), 
            'aadhar' : forms.FileInput(attrs={'required':True}),
            'installmentAmount' : forms.NumberInput(attrs={'required':True}),
            'maturityAmount' : forms.NumberInput(attrs={'required':True}),
            'confirmation' : forms.RadioSelect(choices=confirmationChoices, attrs={'required':True}),
        }