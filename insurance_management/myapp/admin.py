from django.contrib import admin
from .models import Insurances
# Register your models here.

@admin.register(Insurances)
class InsurancesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'policyID', 'dateOfCommencement', 'dateOfMaturity',
    'expiryType', 'insuranceType', 'confirmation', 'aadhar']
    