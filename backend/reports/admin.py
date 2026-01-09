from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import RelatorioMensal

@admin.register(RelatorioMensal)
class RelatorioMensalAdmin(admin.ModelAdmin):
    # Adicionei 'botao_imprimir' na lista
    list_display = ('mes_referencia', 'total_membros', 'saldo_final', 'data_geracao', 'botao_imprimir')
    
    readonly_fields = ('total_membros', 'total_receitas', 'total_despesas', 'saldo_final', 'data_geracao')
    list_filter = ('mes_referencia',)

    # Essa função cria o botão
    def botao_imprimir(self, obj):
        # Gera o link baseado no ID do relatório
        url = reverse('imprimir_relatorio', args=[obj.id])
        
        # Cria um botãozinho HTML
        return format_html(
            '<a class="button" href="{}" target="_blank" style="background-color: #417690; color: white; padding: 5px 10px; border-radius: 5px; text-decoration: none;">🖨️ Imprimir</a>',
            url
        )
    
    botao_imprimir.short_description = "Ações"
    botao_imprimir.allow_tags = True