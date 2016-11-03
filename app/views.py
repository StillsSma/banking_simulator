from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.views.generic import TemplateView, ListView, CreateView
from app.models import Transaction
from app.serializers import TransactionSerializer
#from menu_api.permissions import

class IndexView(TemplateView):

    template_name = "index.html"

class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = "transaction_list.html"
    login_url = '/login/'


    def get_queryset(self):
        return Transaction.objects.filter(account=self.request.user)


class TransactionCreateView(CreateView):
    model = Transaction
    fields = ('amount',)
    success_url = reverse_lazy("transaction_list_view")

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.created_user = self.request.user
        return super().form_valid(form)

class UserCreateView(CreateView):
    model = User
    success_url = reverse_lazy("transaction_list_view")
    form_class = UserCreationForm



class TransactionListCreateAPIView(ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
