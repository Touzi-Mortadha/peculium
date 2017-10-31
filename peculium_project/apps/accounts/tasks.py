# Create your tasks here
# celery worker -A peculium_project -l info -B
from __future__ import absolute_import, unicode_literals
from celery import task
import csv
import os
from django.conf import settings
from celery.utils.log import get_task_logger
from celery.decorators import periodic_task
from datetime import datetime, timedelta
import json
import requests
from ..payment.models import GetCurrency

logger = get_task_logger(__name__)

def Getcurrency():
    url = 'https://min-api.cryptocompare.com/data/price?fsym=EUR&tsyms=BTC,ETH'
    res = json.loads(requests.get(url).content.decode())
    return res['BTC'],res['ETH']

@periodic_task(run_every=timedelta(seconds=5))
def UpdateCurrency():
    model = GetCurrency.objects.get()
    logger.info("Start task ----------------------------------")
    btc, eth = Getcurrency()
    print(btc)
    model.Bitcoin = btc
    model.Ethereum = eth
    model.Euro = 1.0
    model.save()
    logger.info("end of task ----------------------------------")