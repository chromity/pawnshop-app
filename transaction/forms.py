from django import forms
from .models import *


class PawnTransactionForm(forms.ModelForm):
    class Meta:
        model = PawnTransaction
        fields = (
            'first_name', 'middle_name', 'last_name', 'sex', 'nationality', 'contact_number', 'address', 'date_time',
            'code', 'description', 'karat', 'grams', 'percentage', 'price_value', 'current_month_days', 'number_of_days')
