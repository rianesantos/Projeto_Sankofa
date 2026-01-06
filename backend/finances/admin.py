from django.contrib import admin
from .models import FinancialEntry

@admin.register(FinancialEntry)
class FinancialEntryAdmin(admin.ModelAdmin):
    # Colunas que aparecem na lista
    list_display = ('descricao', 'tipo', 'valor', 'categoria', 'data_lancamento', 'tem_comprovante')
    
    # Filtros laterais (MUITO ÚTIL para finanças)
    list_filter = ('tipo', 'data_lancamento', 'categoria')
    
    # Barra de busca
    search_fields = ('descricao', 'categoria')
    
    # Campo de data com navegação rápida no topo
    date_hierarchy = 'data_lancamento'

    # Função extra para mostrar um ícone se tiver comprovante
    def tem_comprovante(self, obj):
        return "Sim" if obj.comprovante else "Não"
    tem_comprovante.short_description = "Tem Nota?"