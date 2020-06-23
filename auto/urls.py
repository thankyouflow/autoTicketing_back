from django.urls import path

from . import views

urlpatterns = [
    path('', views.ticketing.as_view(), name='index'),
]