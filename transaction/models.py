from django.db import models
from datetime import datetime

class PawnTransaction(models.Model):
    # CUSTOMER INFORMATION
    first_name = models.CharField(max_length=256)
    middle_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=128)
    sex = models.CharField(max_length=1, choices=(('M', 'MALE'), ('F', 'FEMALE')))
    nationality = models.CharField(max_length=256)
    contact_number = models.CharField(max_length=64)
    address = models.CharField(max_length=512)

    # PAWN DESCRIPTION
    date_time = models.DateTimeField(default=datetime.now, blank=True)
    code = models.CharField(max_length=256, unique=True)
    description = models.CharField(max_length=1024)
    karat = models.IntegerField(null=True)
    grams = models.IntegerField(null=True)

    # VALUES NEEDED TO COMPUTE A_VALUE
    percentage = models.FloatField(choices=((0.04, '4%'), (0.05, '5%'), (0.06, '6%')))
    price_value = models.FloatField()
    current_month_days = models.IntegerField(default=31, choices=((31, '31'), (30, '30'), (29, '29'), (28, '28')))
    number_of_days = models.FloatField()
    a_value = models.FloatField()
