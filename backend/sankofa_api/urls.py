from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Importamos a função que cria a página de impressão
from reports.views import imprimir_relatorio 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rotas da API (Dados puros para o sistema)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('members.urls')),
    path('api/', include('programs.urls')),
    # (Removi a linha repetida do members.urls que estava aqui)

    # Rota de Impressão (Página visual para humanos)
    path('relatorios/imprimir/<int:report_id>/', imprimir_relatorio, name='imprimir_relatorio'),
]