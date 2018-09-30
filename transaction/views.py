from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . import models
from .forms import *
import logging

# enable logging in this application
logger = logging.getLogger(__name__)


# landing page for transaction application
# require user to login before handling 'index' request
@login_required(login_url='admin:login')
def index(request):
    return render(request, 'transaction/index.html')


# handle transaction list request
@login_required(login_url='admin:login')
def transaction_list(request):
    data = PawnTransaction.objects.order_by('date_time')
    return render(request, 'transaction/transaction_list.html', {'data': data})


# handle transaction detail request
@login_required(login_url='admin:login')
def transaction_detail(request, pk):
    data = get_object_or_404(PawnTransaction, pk=pk)
    return render(request, 'transaction/transaction_detail.html', {'data': data})


# handle transaction add request
@login_required(login_url='admin:login')
def transaction_add(request):
    # query all pawn transactions data to be returned with the add form
    data = PawnTransaction.objects.order_by('date_time')

    if request.method == "POST":
        form = PawnTransactionForm(request.POST)

        if form.is_valid():
            pawn_transaction = form.save(commit=False)

            # if number_of_days is within 2-5
            if 1 < pawn_transaction.number_of_days <= 5:
                pawn_transaction.a_value = ((pawn_transaction.price_value * 0.04) / 30) * pawn_transaction.current_month_days
            elif 5 < PawnTransaction.number_of_days <= 31:
                pawn_transaction.a_value = pawn_transaction.price_value * 0.05
            else:
                # if invalid number_of_day value, return blank form
                form = PawnTransactionForm
                return render(request, 'transaction/transaction_add.html', {'form': form, 'data': data})

            pawn_transaction.save()
    else:
        form = PawnTransactionForm
        return render(request, 'transaction/transaction_add.html', {'form': form, 'data': data})


# handle transaction edit request
@login_required(login_url='admin:login')
def transaction_edit(request, pk):
    pass


# handle transaction delete request\
@login_required(login_url='admin:login')
def transaction_delete(request, pk):
    pass
