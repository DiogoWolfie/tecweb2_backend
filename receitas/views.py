from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from .models import Receita
from .serializers import NoteSerializer
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
      