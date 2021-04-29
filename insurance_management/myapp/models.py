from django.db import models
import datetime
from django.utils import timezone

class Insurances(models.Model):
    policyID = models.CharField(db_column='policyID', max_length=30)
    name = models.CharField(max_length=100, blank=True, null=True)
    insuranceType = models.CharField(db_column='insuranceType', max_length=30, blank=True, null=True)
    dateOfCommencement = models.DateField(db_column='dateOfCommencement')
    expiryType = models.CharField(db_column='expiryType', max_length=30)
    installmentAmount = models.FloatField(db_column='installmentAmount', default=0.0)  # Field name made lowercase.
    maturityAmount = models.FloatField(db_column='maturityAmount', default=0.0)  # Field name made lowercase.
    dateOfMaturity = models.DateField(db_column='dateOfMaturity') 
    aadhar = models.ImageField(upload_to="saved_images")
    confirmation = models.BooleanField(default=False)
    class Meta:
        db_table = 'myapp_insurance'
