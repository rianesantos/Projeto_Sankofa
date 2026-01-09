from django.shortcuts import render, get_object_or_404
from .models import RelatorioMensal

def imprimir_relatorio(request, report_id):
    # Busca o relatório pelo ID
    relatorio = get_object_or_404(RelatorioMensal, id=report_id)
    
    # Manda os dados para o HTML de impressão
    return render(request, 'reports/print_template.html', {'r': relatorio})