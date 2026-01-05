from django.db import models
from django.utils import timezone

# Função para organizar os uploades de comprovantes

def comprovante_upload_path(instance, filename):
    # Salva em 'comprovantes_financeiros/ANO/MES/filename'
    return f"comprovantes_financeiros/{instance.data_lancmento.year} / {instance.data_lancamento.moth} / {filename}"

class FinancialEntry(models.Model):
    """
    Controla receitas e despesas
    """
    TIPO_LANCAMENTO_CHOICES = [
        ('RECEITA', 'Receita'),
        ('DESPESA', 'Despesa'),
    ]
    
    tipo = models.CharField(
        max_length = 7,
        choices = TIPO_LANCAMENTO_CHOICES,
        verbose_name="Tipo de Lançamento"
    )
    
    descriacao = models.CharField(max_length=255, verbose_name="Descrição")
    
    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Valor (R$)"
    )
    
    data_lancamento = models.DateField(
        default=timezone.now,
        verbose_name="Data do Lançamento"
    )
    
    # Este campo pode ser usado para 'Doação', 'Patrocínio', 'Conta de Luz', 'Material', etc.
    categoria = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Categoria"
    )
    
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação no Sistema")
    
    def __str__(self):
        return f"[{self.get_tipo_display()}] {self.descricao} - R$ {self.valor}"
    
    class Meta:
        verbose_name = "Lançamento Financeiro"
        verbose_name_plural = "Lançamentos Financeiros" 
        # Ordena os lançamentos mais recentes primeiro
        ordering = ['-data_lancamento']