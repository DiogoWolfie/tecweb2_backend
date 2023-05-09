from rest_framework import serializers
from .models import Receita


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = ['receita']