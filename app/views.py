from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from app.models import Transaction
from app.serializers import TransactionSerializer
from app.permissions import IsAuthenticated
#from menu_api.permissions import


class TransactionListCreateAPIView(ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated, )
