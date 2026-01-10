from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MemberViewSet, DocumentoViewSet

# Cria o gerenciador de rotas
router = DefaultRouter()

# Registra os endereços
# Ex: site.com/api/members/
router.register(r'members', MemberViewSet) 
# Ex: site.com/api/documentos/
router.register(r'documentos', DocumentoViewSet)

urlpatterns = [
    # Inclui todas as rotas que o router criou automaticamente
    path('', include(router.urls)),
]