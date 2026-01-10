from rest_framework import serializers
# O ponto (.) significa "desta mesma pasta"
from .models import Member, Documento  # <--- Confirme se o nome do model é Documento ou DocumentoMembro no seu models.py

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'  # Pega TUDO (nome, cpf, foto, data...) automaticamente

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        # Importante: Confirme se o nome da classe no models.py é 'Documento' ou 'DocumentoMembro'
        model = Documento 
        fields = '__all__'