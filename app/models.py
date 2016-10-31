from django.db import models

class Transaction(models.Model):
    amount = models.FloatField()
    time_created = models.DateTimeField(auto_now_add=True)
    account = models.ForeignKey('auth.User')

    @property
    def is_credit(self):
        return self.amount > 0
