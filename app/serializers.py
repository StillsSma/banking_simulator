from rest_framework import serializers
from app.models import Transaction, Profile

class TransactionSerializer(serializers.ModelSerializer):

    is_deposit = serializers.ReadOnlyField()

    class Meta:
        model = Transaction
        exclude = ('account',)
class ProfileSerializer(serializers.ModelSerializer):


    class Meta:
        model = Profile
        fields = '__all__'
