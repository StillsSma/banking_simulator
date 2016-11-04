from django.db import models
from django.db.models import Sum


class Transaction(models.Model):
    amount = models.FloatField()
    time_created = models.DateTimeField(auto_now_add=True)
    account = models.ForeignKey('auth.User')
    checking = models.BooleanField(default=True)

    @property
    def is_credit(self):
        return self.amount > 0

    @property
    def checking_balance(self):
        return Transaction.objects.filter(checking=True).aggregate(balance=Sum('amount'))
    @property
    def checking_balance(self):
        return Transaction.objects.filter(checking=True).aggregate(balance=Sum('amount'))
