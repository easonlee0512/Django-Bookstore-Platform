from decimal import Decimal

from django.conf import settings
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt


from orders.models import Order


def payment_process(request):
    return render(request,
                  'payment/process.html')
    

