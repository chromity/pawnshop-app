from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
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

            number_of_days = pawn_transaction.number_of_days
            # if number_of_days is within 2-5
            if 1 < number_of_days <= 5:
                pawn_transaction.a_value = ((pawn_transaction.price_value * 0.04) / 30) * pawn_transaction.current_month_days
            elif 5 < number_of_days <= 31:
                pawn_transaction.a_value = pawn_transaction.price_value * 0.05
            else:
                # if invalid number_of_day value, return blank form
                form = PawnTransactionForm
                return render(request, 'transaction/transaction_add.html', {'form': form, 'data': data})

            # save the request
            pawn_transaction.save()

            # return the user once again to the form
            form = PawnTransactionForm
            return render(request, 'transaction/transaction_add.html', {'form': form, 'data': data})
    else:
        form = PawnTransactionForm
        return render(request, 'transaction/transaction_add.html', {'form': form, 'data': data})


# handle transaction edit request
@login_required(login_url='admin:login')
def transaction_edit(request, pk):
    # query all pawn transactions data to be returned with the add form
    data = PawnTransaction.objects.order_by('date_time')

    # get pawn_transaction data that will be edited base from the primary key in the request
    pawn_transaction = get_object_or_404(PawnTransaction, pk=pk)
    logger.info(pawn_transaction)

    if request.method == "POST":
        # insert queried data to the form template
        form = PawnTransactionForm(request.POST, instance=pawn_transaction)

        if form.is_valid():
            pawn_transaction = form.save(commit=False)

            number_of_days = pawn_transaction.number_of_days
            # if number_of_days is within 2-5
            if 1 < number_of_days <= 5:
                pawn_transaction.a_value = ((pawn_transaction.price_value * 0.04) / 30) * pawn_transaction.current_month_days
            elif 5 < number_of_days <= 31:
                pawn_transaction.a_value = pawn_transaction.price_value * 0.05
            else:
                # if invalid number_of_day value, return blank form
                form = PawnTransactionForm
                return render(request, 'transaction/transaction_edit.html', {'form': form, 'data': data})

            pawn_transaction.save()

            form = PawnTransactionForm
            return render(request, 'transaction/transaction_edit.html', {'form': form, 'data': data})
    else:
        form = PawnTransactionForm(instance=pawn_transaction)
        return render(request, 'transaction/transaction_edit.html', {'form': form, 'data': data})


# handle transaction delete request\
@login_required(login_url='admin:login')
def transaction_delete(request, pk):
    # delete pawn_transaction when delete request is received from the view
    pawn_transaction = get_object_or_404(PawnTransaction, pk=pk)
    pawn_transaction.delete()

    data = PawnTransaction.objects.order_by('date_time')
    form = PawnTransactionForm
    return render(request, 'transaction/transaction_add.html', {'form': form, 'data': data})