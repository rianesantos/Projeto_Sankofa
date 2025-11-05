from rest_framework import serializers
from .models import Program, Enrollment
from members.serializers import MemberSerializer

class ProgramSerializer(serializers.ModelSerializer):   
    
    class Meta:
        model = Program
        fields = [
            'id',
            'nome',
            'tipo',
            'descricao',  
            'regras_elegibilidade',
            'data_inicio',
            'data_fim',
        ]
        
class EnrollmentSerializer(serializers.ModelSerializer):
    
    # Estes campos 'read_only=True' são para mostrar os *detalhes*
    # do membro e do programa, em vez de só os seus IDs.
    membro = MemberSerializer(read_only=True)
    programa = ProgramSerializer(read_only=True)
    
    # Estes campos 'write_only=True' são os que usamos para
    # *criar* uma nova inscrição, enviando apenas os IDs.
    membro_id = serializers.IntegerField(write_only=True)
    programa_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Enrollment
        fields = [
            'id',
            'membro', # Detalhes do membro (leitura)
            'programa', # Detalhes do programa (leitura)
            'membro_id', # ID para criar (escrita)
            'programa_id', # ID para criar (escrita)
            'data_inscricao',
            'status',
            'observacoes',
        ]
        
        def create(self, validated_data):
            return Enrollment.objects.create(
                membro_id=validated_data['membro_id'],
                programa_id=validated_data['programa_id'],
                status=validated_data.get('status', 'PENDENTE'),
                observacoes=validated_data.get('observacoes', None)
            )