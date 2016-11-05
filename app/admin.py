from django.contrib import admin

# Register your models here.
from app.models import Transaction, Profile

admin.site.register(Transaction)
admin.site.register(Profile)
