from django.db import models

class Insurances(models.Model):
    policyID = models.IntegerField(db_column='policyID', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    insuranceType = models.CharField(db_column='insuranceType', max_length=30, blank=True, null=True)
    dateOfCommencement = models.DateField(db_column='dateOfCommencement')
    expiryType = models.CharField(db_column='expiryType', max_length=30)
    installmentAmount = models.FloatField(db_column='installmentAmount', default=0.0)
    maturityAmount = models.FloatField(db_column='maturityAmount', default=0.0)
    dateOfMaturity = models.DateField(db_column='dateOfMaturity') 
    aadhar = models.ImageField(upload_to="saved_images")
    confirmation = models.BooleanField(default=False)
    comments=models.CharField(max_length=300, db_column='comments', default='')
    class Meta:
        db_table = 'myapp_insurance'