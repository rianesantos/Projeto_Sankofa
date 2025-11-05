from django.db import models

def get_profile_image_path(instance, filename):
    return f'fotos_membros/{instance.cpf}/{filename}'

class Member(models.Model):
    nome_completo = models.CharField(max_length=255, verbose_name='Nome Completo')
    cpf = models.CharField(max_length=14, unique=True, verbose_name='CPF')
    rg = models.CharField(max_length=20, unique=True, verbose_name='RG')
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    endereco = models.CharField(max_length=255, verbose_name='Endereço')
    telefone_contato = models.CharField(max_length=20, verbose_name='Telefone de Contato')
    email = models.EmailField(blank=True, null=True, verbose_name='Email')
    foto_perfil = models.ImageField(upload_to=get_profile_image_path, blank=True, null=True, verbose_name="Foto de Perfil")
    # Para outros comprovantes, criar um modelo separado no futuro.

    # Controle de Situação
    SITUACAO_CHOICES = [
        ('REGULAR', 'Regular'),
        ('IRREFULAR', 'Irregular'),
        ('PENDENTE', 'Pendente'),
    ]
    situacao = models.CharField(
        max_length=10,
        choices=SITUACAO_CHOICES,
        default='PENDENTE',
        verbose_name='Situação do Membro'
        )
    
    # Datas de controle
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name='Data de Cadastro')
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name='Ultima Atualização')
    
    parentes = models.ManyToManyField(
        'self',
        blank=True,
        symmetrical=False,
        verbose_name='Parentes'
    )
    
    def __str__(self):
        return f"{self.nome_completo} (CPF: {self.cpf})"
    
    class Meta:
        verbose_name = "Membro"
        verbose_name_plural = "Membros"
    
def comprovante_upload_path(instance, filename):
    return f'documentos_membros/{instance.member.cpf}/{filename}'

class Documento(models.Model):
    """
    Modelo para upload de múltiplos documentos (comprovantes)
    para um único Membro
    """
    
    membro = models.ForeignKey(
        Member,
        on_delete=models.CASCADE, # Se o membro for deletado, seus docs também são.
        related_name="documentos", # Como vamos acessar os docs (ex: membro.documentos.all())
        verbose_name="Membro"
    )
    
    descricao = models.CharField(max_length=100, verbose_name="Descrição do Documento")
    arquivo = models.FileField(
        upload_to=comprovante_upload_path,
        verbose_name="Arquivo (PDF, Imagem)"
    )
    data_upload = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Documento: {self.descricao} para {self.membro.nome_completo}"
    
    class Meta:
        verbose_name = "Documento do Membro"
        verbose_name_plural = "Documentos dos Membros"