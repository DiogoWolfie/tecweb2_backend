from django.urls import path

from . import views

urlpatterns = [
    path('api/receitas/', views.api_save),
]