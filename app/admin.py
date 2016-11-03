from django.contrib import admin

# Register your models here.
from app.models import Transaction

admin.site.register(Transaction)
