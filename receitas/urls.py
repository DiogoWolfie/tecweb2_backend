from django.urls import path

from . import views

urlpatterns = [
    path('api/receitas/', views.api_save),
    #path("api/log/", views.Log_save),
    path("api/livros/",views.Livro_save),
]