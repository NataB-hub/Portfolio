from django.urls import path
from main_list import views

urlpatterns = [
    path('', views.main_list, name='main_list'),
]