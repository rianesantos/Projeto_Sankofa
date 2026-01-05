from django.db import models

def get_profile_image_path(instance, filename): # Função para definir o caminho de upload da foto de perfil
    return f'fotos_membros/{instance.cpf}/{filename}' # Organiza as fotos por CPF do membro

class Member(models.Model): # Modelo para representar um membro da organização 
    nome_completo = models.CharField(max_length=255, verbose_name='Nome Completo') # Nome completo do membro
    cpf = models.CharField(max_length=14, unique=True, verbose_name='CPF') # CPF único do membro
    rg = models.CharField(max_length=20, unique=True, verbose_name='RG') # RG único do membro
    data_nascimento = models.DateField(verbose_name='Data de Nascimento') # Data de nascimento do membro
    endereco = models.CharField(max_length=255, verbose_name='Endereço') # Endereço do membro
    telefone_contato = models.CharField(max_length=20, verbose_name='Telefone de Contato') # Telefone de contato do membro
    email = models.EmailField(blank=True, null=True, verbose_name='Email') # Email do membro (opcional?)
    foto_perfil = models.ImageField(upload_to=get_profile_image_path, blank=True, null=True, verbose_name="Foto de Perfil") # Foto de perfil do membro (opcional)
    # Para outros comprovantes, criar um modelo separado no futuro.

    # Controle de Situação
    SITUACAO_CHOICES = [ # Opções para o campo de situação do membro
        ('REGULAR', 'Regular'),
        ('IRREFULAR', 'Irregular'),
        ('PENDENTE', 'Pendente'),
    ]
    situacao = models.CharField( # Campo para armazenar a situação do membro
        max_length=10,
        choices=SITUACAO_CHOICES,
        default='PENDENTE',
        verbose_name='Situação do Membro' # Descrição da situação do membro
        )
    
    # Datas de controle
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name='Data de Cadastro') # Data de cadastro do membro
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name='Ultima Atualização') # Data da última atualização do membro
    
    parentes = models.ManyToManyField( # Relação de parentesco entre membros
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
    
def comprovante_upload_path(instance, filename): # Função para definir o caminho de upload dos documentos
    return f'documentos_membros/{instance.membro.cpf}/{filename}'

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
    
    descricao = models.CharField(max_length=100, verbose_name="Descrição do Documento") # Descrição do documento
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