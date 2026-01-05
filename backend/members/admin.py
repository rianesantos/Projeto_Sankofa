from django.contrib import admin
from .models import Member, Documento

# Configuração para ver os Documentos DENTRO da tela do Membro
class DocumentoInline(admin.TabularInline):
    model = Documento
    extra = 1  # Deixa um espaço em branco pronto para adicionar

# Configuração da Tabela de Membros
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    # O que vai aparecer nas colunas da tabela
    list_display = ('nome_completo', 'cpf', 'situacao', 'telefone_contato', 'data_atualizacao')
    
    # Filtros laterais (barra direita)
    list_filter = ('situacao', 'data_cadastro')
    
    # Barra de pesquisa (topo) - Pesquisa por nome ou CPF
    search_fields = ('nome_completo', 'cpf', 'rg')
    
    # Adiciona a área de documentos dentro do membro
    inlines = [DocumentoInline]

# Configuração simples para os Documentos (caso queira ver separado)
@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'membro', 'data_upload')