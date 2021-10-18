from django.db import models


class ExchangeRate(models.Model):
    from_currency_name = models.CharField(blank=True, max_length=255)
    to_currency_name = models.CharField(blank=True, max_length=255)
    exchange_rate = models.DecimalField(max_digits=8)

