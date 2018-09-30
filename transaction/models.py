from django.db import models


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
    date_time = models.DateTimeField()
    code = models.CharField(max_length=256, unique=True)
    description = models.TextField(max_length=2048)
    karat = models.IntegerField(null=True)
    grams = models.IntegerField(null=True)

    # VALUES NEEDED TO COMPUTE A_VALUE
    percentage = models.FloatField(choices=((0.04, '4%'), (0.05, '5%'), (0.06, '6%')))
    price_value = models.FloatField()
    number_of_days = models.FloatField()
    a_value = models.FloatField()
