from django.urls import path

from . import views

urlpatterns = [
    path('ticketing/', views.ticketing.as_view(), name='index'),
    path('login/', views.login_check.as_view(), name='index'),
]