from rest_framework import generics
from .models import Member, Documento
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import MemberSerializer, DocumentoSerializer

class MemberListCreateViewSet(generics.ListCreateAPIView):
    queryset = Member.objects.all().order_by('nome_completo')
    serializer_class = MemberSerializer
    
class DocumentoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
    parser_classes = [MultiPartParser, FormParser]