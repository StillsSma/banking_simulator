from rest_framework import serializers
from app.models import Transaction

class TransactionSerializer(serializers.ModelSerializer):

    is_deposit = serializers.ReadOnlyField()

    class Meta:
        model = Transaction
        fields = '__all__'
