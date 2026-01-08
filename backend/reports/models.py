from django.db import models
from django.db.models import Sum
from django.utils import timezone
from decimal import Decimal  # <--- IMPORTANTE

from members.models import Member
from finances.models import FinancialEntry

class RelatorioMensal(models.Model):
    mes_referencia = models.DateField(default=timezone.now, verbose_name="Mês de Referência")
    
    total_membros = models.IntegerField(default=0, verbose_name="Total de Membros")
    total_receitas = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_despesas = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    saldo_final = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    data_geracao = models.DateTimeField(auto_now_add=True, verbose_name="Gerado em")

    def save(self, *args, **kwargs):
        self.total_membros = Member.objects.count()
        
        ano = self.mes_referencia.year
        mes = self.mes_referencia.month

        # A CORREÇÃO ESTÁ AQUI EMBAIXO 
        # Se não tiver valor, usamos Decimal('0.00') em vez de 0.00 solto

        soma_receitas = FinancialEntry.objects.filter(
            tipo='RECEITA',
            data_lancamento__year=ano,
            data_lancamento__month=mes
        ).aggregate(Sum('valor'))['valor__sum']
        
        # Se a soma for None (vazio), assume Decimal zero
        receitas = soma_receitas if soma_receitas else Decimal('0.00')

        soma_despesas = FinancialEntry.objects.filter(
            tipo='DESPESA',
            data_lancamento__year=ano,
            data_lancamento__month=mes
        ).aggregate(Sum('valor'))['valor__sum']

        # Se a soma for None (vazio), assume Decimal zero
        despesas = soma_despesas if soma_despesas else Decimal('0.00')

        self.total_receitas = receitas
        self.total_despesas = despesas
        self.saldo_final = receitas - despesas # Agora Decimal conversa com Decimal!

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Relatório Financeiro - {self.mes_referencia.strftime('%m/%Y')}"

    class Meta:
        verbose_name = "Relatório Mensal"
        verbose_name_plural = "Relatórios Mensais"