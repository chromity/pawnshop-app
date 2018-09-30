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
    pass


# handle transaction detail request
@login_required(login_url='admin:login')
def transaction_detail(request):
    pass


# handle transaction add request
@login_required(login_url='admin:login')
def transaction_add(request):
    pass


# handle transaction edit request
@login_required(login_url='admin:login')
def transaction_edit(request, pk):
    pass


# handle transaction delete request\
@login_required(login_url='admin:login')
def transaction_delete(request, pk):
    pass