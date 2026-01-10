from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Member, Documento
from .serializers import MemberSerializer, DocumentoSerializer

class MemberViewSet(viewsets.ModelViewSet):
    # O ModelViewSet cria sozinho as rotas de: Listar, Criar, Editar e Deletar
    queryset = Member.objects.all().order_by('nome_completo')
    serializer_class = MemberSerializer
    # Isso aqui é essencial para o botão de upload de foto funcionar
    parser_classes = [MultiPartParser, FormParser]

class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
    parser_classes = [MultiPartParser, FormParser]