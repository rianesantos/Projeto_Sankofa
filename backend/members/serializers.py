from rest_framework import serializers
from .models import Member, Documento

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Member
        
        fields = [
            'id',
            'nome_completo',
            'email',
            'cpf',
            'rg',
            'data_nascimento',
            'situacao',
            'telefone_contato',
            'data_cadastro',
            'parentes'
        ]
        
class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = [
            'id',
            'membro', # O ID do membro ao qual o doc pertence
            'arquivo', # O arquivo do documento
            'descricao',
            'data_upload'
        ]