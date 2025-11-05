from django.db import models
from members.models import Member # Importação correta

class Program(models.Model):
    """
    Modelo para o Cadastro de Programas e Benefícios (Requisito 2.2).
    Ex: bolsas, auxílios, eventos.
    """

    # Tipos de programa para facilitar a filtragem
    TIPO_PROGRAMA_CHOICES = [
        ('BOLSA', 'Bolsa'),
        ('AUXILIO', 'Auxílio'),
        ('EVENTO', 'Evento'),
        ('OUTRO', 'Outro'),
    ]

    nome = models.CharField(max_length=200, verbose_name='Nome do Programa')
    
    tipo = models.CharField(max_length=10, choices=TIPO_PROGRAMA_CHOICES, default='OUTRO')

    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição do Programa')

    regras_elegibilidade = models.TextField(blank=True, null=True, verbose_name='Regras de Elegibilidade')

    data_inicio = models.DateField(blank=True, null=True, verbose_name='Data de Início')
    data_fim = models.DateField(blank=True, null=True, verbose_name='Data de Fim')

    # Este campo vai ligar os Membros a este Programa,
    # usando o modelo 'Enrollment' (abaixo) como ponte
    membros_partipantes = models.ManyToManyField(
        Member,
        through='Enrollment',
        related_name='programas_participantes',
        blank=True
    )

    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       
        return f"[{self.get_tipo_display()}] {self.nome}"

    class Meta:
        verbose_name = "Programa"
        verbose_name_plural = "Programas"

class Enrollment(models.Model):
    """
    Modelo de Ligação (through model) que implementa:
    - Vinculação de membros a programas
    - Registro de benefícios recebidos
    """

    STATUS_BENEFICIO_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('APROVADO', 'Aprovado'),
        ('RECEBIDO', 'Benefício Recebido'), 
        ('REJEITADO', 'Rejeitado'),
    ]

    # As duas chaves estrangeiras que fazem a ligação
    membro = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='inscricoes')
    programa = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='inscricoes')


    data_inscricao = models.DateTimeField(auto_now_add=True, verbose_name='Data de Inscrição')
    
    status = models.CharField(
        max_length=10,
        choices=STATUS_BENEFICIO_CHOICES,
        default='PENDENTE',
        verbose_name='Status do Benefício'
    )

    observacoes = models.TextField(blank=True, null=True, verbose_name='Observações')
    
    def __str__(self):
        return f"{self.membro.nome_completo} inscrito em {self.programa.nome}"

    class Meta:
        # Garantir que um membro não possa se inscrever no mesmo programa mais de uma vez
        unique_together = ('membro', 'programa')
        verbose_name = "Inscrição"
        verbose_name_plural = "Inscrições"