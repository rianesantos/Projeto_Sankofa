from django.contrib import admin
from .models import RelatorioMensal

@admin.register(RelatorioMensal)
class RelatorioMensalAdmin(admin.ModelAdmin):
    # Mostra as colunas com os resultados
    list_display = ('mes_referencia', 'total_membros', 'saldo_final', 'data_geracao')
    
    # Deixa esses campos apenas como leitura (para ninguém fraudar o relatório manualmente)
    readonly_fields = ('total_membros', 'total_receitas', 'total_despesas', 'saldo_final', 'data_geracao')
    
    list_filter = ('mes_referencia',)