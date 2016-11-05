from django.db import models
from django.dispatch import receiver
from django.db.models import Sum
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField('auth.User')

    def __str__(self):
        return str(self.id)

    @receiver(post_save, sender='auth.user')
    def create_profile(sender, **kwargs):
        instance = kwargs["instance"]
        created = kwargs["created"]
        if created:
            Profile.objects.create(user=instance)
    def transactions(self):
        return Transaction.objects.filter(account=self)

    def balance(self):
        try:
            return round(Transaction.objects.filter(account=self).aggregate(balance=Sum('amount'))['balance'], 2)
        except TypeError:
            return None

class Transaction(models.Model):
    amount = models.FloatField()
    time_created = models.DateTimeField(auto_now_add=True)
    account = models.ForeignKey(Profile)

    @property
    def is_credit(self):
        return self.amount > 0
