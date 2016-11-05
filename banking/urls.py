
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.authtoken import views
from django.views.generic import TemplateView
from app.views import TransactionListCreateAPIView, ProfileView, TransactionCreateView, UserCreateView, IndexView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^obtain-token/$', views.obtain_auth_token),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^profile/(?P<pk>\d+)$', ProfileView.as_view(), name="profile_view"),
    url(r'^profile/(?P<pk>\d+)/create/$', TransactionCreateView.as_view(), name="transaction_create_view"),
    url(r'^api/transactions/create$', TransactionListCreateAPIView.as_view(), name="transaction_list_api_view" ),
    url(r'^create_user/$', UserCreateView.as_view(), name="user_create_view"),

]
