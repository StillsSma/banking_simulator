from django.db import models
from django.dispatch import receiver
from django.db.models import Sum
from django.db.models.signals import post_save
from django.conf import settings
from rest_framework.authtoken.models import Token

import random

class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    account_number = models.CharField(max_length=4, unique=True)

    def __str__(self):
        return str(self.id)

    @receiver(post_save, sender='auth.user')
    def create_profile(sender, **kwargs):
        instance = kwargs["instance"]
        created = kwargs["created"]
        if created:
            r = random.randint(1111,9999)
            Profile.objects.create(user=instance, account_number=r)

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
       if created:
           Token.objects.create(user=instance)
    def transactions(self):
        return Transaction.objects.filter(account=self).order_by('-time_created')

    def balance(self):
        credits = Transaction.objects.filter(account=self, withdrawl_or_deposit='Credit')
        credit_total = sum([item.amount for item in credits])
        debits = Transaction.objects.filter(account=self, withdrawl_or_deposit='Debit')
        debit_total = sum([item.amount for item in debits])
        return round( (credit_total - debit_total), 2)



deposit = 'Credit'
withdrawl = 'Debit'
CHOICES = [
(withdrawl, 'withdrawl'),
(deposit, 'deposit')
]

class Transaction(models.Model):

    withdrawl_or_deposit = models.CharField(max_length=7, choices=CHOICES)
    amount = models.FloatField()
    time_created = models.DateTimeField(auto_now_add=True)
    account = models.ForeignKey(Profile)
