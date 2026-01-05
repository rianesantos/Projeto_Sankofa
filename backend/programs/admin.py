from django.contrib import admin
from .models import Program, Enrollment

# Configuração para ver as Inscrições DENTRO da tela do Programa
class EnrollmentInline(admin.TabularInline):
    model = Enrollment
    extra = 1
    # autocomplete_fields = ['membro'] # Habilitar se tiver muitos membros no futuro

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    # Campos que existem no SEU modelo atual
    list_display = ('nome', 'tipo', 'data_inicio') 
    list_filter = ('tipo',) 
    search_fields = ('nome',)
    inlines = [EnrollmentInline] # Conecta a lista de inscritos dentro do programa

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('membro', 'programa', 'status', 'data_inscricao')
    list_filter = ('status', 'programa')
    search_fields = ('membro__nome_completo', 'programa__nome')