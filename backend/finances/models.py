from django.db import models
from django.utils import timezone

# Função para organizar os uploads de comprovantes
def comprovante_upload_path(instance, filename):
    # Salva em 'comprovantes_financeiros/2026/01/nota.pdf'
    # Correção: data_lancamento e month
    return f"comprovantes_financeiros/{instance.data_lancamento.year}/{instance.data_lancamento.month}/{filename}"

class FinancialEntry(models.Model):
    """
    Controla receitas e despesas (O Livro Caixa)
    """
    TIPO_LANCAMENTO_CHOICES = [
        ('RECEITA', 'Receita (Entrada)'),
        ('DESPESA', 'Despesa (Saída)'),
    ]
    
    tipo = models.CharField(
        max_length=10, # Aumentei um pouco por segurança
        choices=TIPO_LANCAMENTO_CHOICES,
        verbose_name="Tipo de Lançamento"
    )
    
    descricao = models.CharField(max_length=255, verbose_name="Descrição (Ex: Conta de Luz)")
    
    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Valor (R$)"
    )
    
    data_lancamento = models.DateField(
        default=timezone.now,
        verbose_name="Data do Lançamento"
    )
    
    # Campo Categoria (Texto simples por enquanto)
    categoria = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Categoria (Ex: Alimentação, Transporte)"
    )

    # O CAMPO NOVO QUE FALTAVA! 👇
    comprovante = models.FileField(
        upload_to=comprovante_upload_path,
        blank=True,
        null=True,
        verbose_name="Comprovante / Nota Fiscal"
    )
    
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    
    def __str__(self):
        # Ex: [DESPESA] Conta de Luz - R$ 150.00
        return f"[{self.tipo}] {self.descricao} - R$ {self.valor}"
    
    class Meta:
        verbose_name = "Lançamento Financeiro"
        verbose_name_plural = "Lançamentos Financeiros"
        ordering = ['-data_lancamento']