from django.contrib import admin
from .models import Insurances
# Register your models here.

@admin.register(Insurances)
class InsurancesAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'date']