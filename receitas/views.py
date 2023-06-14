from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from .models import Receita, Log, Livro
from .serializers import NoteSerializer, LogSerializer, LivroSerializer
from django.http import Http404
#def index(request):
#    return HttpResponse("Olá mundo! Este é o app notes de Tecnologias Web do Insper.")

# Create your views here.


@api_view(['GET','POST'])
def api_save(request):
    if request.method == 'POST':
        new_data = request.data
        receita = Receita()
        receita.receita = new_data["receitas"]
        receita.save()
    all_receitas = Receita.objects.all()

    serialized_note = NoteSerializer(all_receitas, many = True) #converter para json
    return Response(serialized_note.data)

# @api_view(['GET','POST'])    
# def Log_save(request):
#     #try:
#      #   log = Log.objects.get(IP = note_ip)
#     #except Log.DoesNotExist:
#      #   raise Http404()    

#     if request.method == "POST":
#         new_log = request.data
#         log = Log()
#         log.IP = new_log["IP"]
#         log.acesso = new_log["acesso"]
#         log.latitude = new_log["latitude"]
#         log.longitude = new_log["longitude"]
#         log.sistema = new_log["sistema"]
#         log.save()
        
#     all_logs = Log.objects.all()

#     serialized_log = LogSerializer(all_logs, many = True)
#     print(serialized_log)
#     return Response(serialized_log.data)

@api_view(['GET','POST'])    
def Livro_save(request):
    
    if request.method == "POST":
        new_livro = request.data
        livro = Livro()
        livro.titulo = new_livro["titulo"]
        livro.isbn = new_livro["isbn"]
        livro.editora = new_livro["editora"]
        livro.autor = new_livro["autor"]
        livro.versao_fisica = new_livro["versao_fisica"]
        livro.save()

        all_livros = Livro.objects.all()
        serialized_livro = LivroSerializer(all_livros, many = True)
        return Response(serialized_livro.data)

    if request.method == "GET":
        all_livros = Livro.objects.all()
        serialized_livro = LivroSerializer(all_livros, many = True)
        return Response(serialized_livro.data)

    
