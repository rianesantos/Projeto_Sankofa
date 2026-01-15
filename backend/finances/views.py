from rest_framework import viewsets
from .models import FinancialEntry
from .serializers import FinancialEntrySerializer

class FinancialEntryViewSet(viewsets.ModelViewSet):
    # Pega todos os lançamentos e ordena do mais recente para o antigo
    queryset = FinancialEntry.objects.all().order_by('-data_lancamento')
    serializer_class = FinancialEntrySerializer