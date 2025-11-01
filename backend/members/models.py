from django.db import models

def get_profile_image_path(instance, filename):
    return f'fotos_membros/{instance.cpf}/{filename}'

class Member(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome Completo')
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
    
   # 5. Relacionamentos
    # Estes campos serão adicionados depois de criar os outros modelos,
    # como 'Programs' e a lógica de 'Parentesco'.
    # historico_programas = ...
    # parentes = ... 
    
    def __str__(self):
        return f"{self.nome_completo} (CPF: {self.cpf})"
    
    class Meta:
        verbose_name = "Membro"
        verbose_name_plural = "Membros"