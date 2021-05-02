from django.db import models


class InsuranceType(models.Model):
    value = models.CharField(primary_key=True, max_length=30)

    class Meta:
        # managed = False
        db_table = 'Insurance_Type'

class Insurances(models.Model):
    policyID = models.IntegerField(db_column='policyID', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    # insurancetype = models.ForeignKey(InsuranceType, models.DO_NOTHING, db_column='insuranceType', blank=True, null=True)
    # insuranceType = models.ManyToManyField(InsuranceType)
    insuranceType = models.CharField(db_column='insuranceType', max_length=30, blank=True, null=True)
    dateOfCommencement = models.DateField(db_column='dateOfCommencement')
    expiryType = models.CharField(db_column='expiryType', max_length=30)
    installmentAmount = models.FloatField(db_column='installmentAmount', default=0.0)  # Field name made lowercase.
    maturityAmount = models.FloatField(db_column='maturityAmount', default=0.0)  # Field name made lowercase.
    dateOfMaturity = models.DateField(db_column='dateOfMaturity') 
    aadhar = models.ImageField(upload_to="saved_images")
    confirmation = models.BooleanField(default=False)
    comments=models.CharField(max_length=300, db_column='comments')
    class Meta:
        db_table = 'myapp_insurance'

# class MyappInsurance(models.Model):
#     aadhar = models.CharField(max_length=100)
#     dateofcommencement = models.DateField(db_column='dateOfCommencement')  # Field name made lowercase.
#     dateofmaturity = models.DateField(db_column='dateOfMaturity')  # Field name made lowercase.
#     policyid = models.CharField(db_column='policyID', max_length=30)  # Field name made lowercase.
#     expirytype = models.CharField(db_column='expiryType', max_length=30)  # Field name made lowercase.
#     confirmation = models.BooleanField()
#     insurancetype = models.ForeignKey(InsuranceType, models.DO_NOTHING, db_column='insuranceType', blank=True, null=True)  # Field name made lowercase.
#     name = models.CharField(max_length=100, blank=True, null=True)
#     installmentamount = models.FloatField(db_column='installmentAmount')  # Field name made lowercase.
#     maturityamount = models.FloatField(db_column='maturityAmount')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'myapp_insurance'

