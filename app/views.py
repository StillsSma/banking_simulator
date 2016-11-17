from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from app.models import Transaction, Profile
from app.serializers import TransactionSerializer, ProfileSerializer
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from app.permissions import IsCreatedBy, Post


#from menu_api.permissions import

class IndexView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context['profile'] = get_object_or_404(Profile, user=self.request.user)

        return context




class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(user=self.request.user)
        if self.kwargs['pk'] != str(self.request.user.profile):
            raise PermissionDenied
        return context

class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    login_url = '/login/'
    fields = ('amount', 'withdrawl_or_deposit')

    def get_success_url(self,**kwargs):
        var = Profile.objects.get(user=self.request.user)
        return reverse_lazy("profile_view", args=[var.id])
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.account = Profile.objects.get(user=self.request.user)
        if instance.withdrawl_or_deposit == "Debit":
            if Profile.objects.get(user=self.request.user).balance() - instance.amount < 0 :
                return self.form_invalid(form)

        return super().form_valid(form)



class UserCreateView(CreateView):
    model = User
    success_url = reverse_lazy("index_view")
    form_class = UserCreationForm


class TransactionListCreateAPIView(ListCreateAPIView):
    def get_queryset(self):
        return Transaction.objects.filter(account=self.request.user.profile)
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated,)

class TransactionRetrieveAPIView(RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (IsCreatedBy, )
