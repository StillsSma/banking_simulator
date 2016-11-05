from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from app.models import Transaction, Profile
from app.serializers import TransactionSerializer
from django.core.exceptions import PermissionDenied
from django.contrib import messages


#from menu_api.permissions import

class IndexView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        try:
            context['profile'] = Profile.objects.get(user=self.request.user)
        except TypeError:
            pass
        return context

class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(user=self.request.user)
        if self.kwargs['pk'] != str(self.request.user.profile):
            raise PermissionDenied



        return context

class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    login_url = '/login/'
    fields = ('amount',)

    def get_success_url(self,**kwargs):
        var = Profile.objects.get(user=self.request.user)
        return reverse_lazy("profile_view", args=[var.id])


    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.account = Profile.objects.get(user=self.request.user)
        if instance.amount == 0 or Profile.objects.get(user=self.request.user).balance() + instance.amount < 0 :
            return self.form_invalid(form)
        return super().form_valid(form)

class UserCreateView(CreateView):
    model = User
    success_url = reverse_lazy("index_view")
    form_class = UserCreationForm



class TransactionListCreateAPIView(ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
