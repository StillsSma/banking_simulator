from django.db import models

class Account(models.Model):
    user = models.ForeignKey('auth.User')

    def balance(self):
        return 


class Transaction(models.Model):
    amount = models.FloatField()
    time_created = models.DateTimeField(auto_now_add=True)
    account = models.ForeignKey(Account)

    @property
    def is_credit(self):
        return self.amount > 0
