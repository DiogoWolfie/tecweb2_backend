from rest_framework import serializers
from .models import Receita, Log, Livro


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = ['receita']

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ['IP', "acesso", "latitude", "longitude", "sistema"]


class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ['titulo', "isbn", "editora", "autor", "versao_fisica"]
