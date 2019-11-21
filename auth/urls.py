from django.contrib import admin
from django.urls import path
from .views import login, auth_test


urlpatterns = [
    path('login', login),
    path('auth-test', auth_test)
]