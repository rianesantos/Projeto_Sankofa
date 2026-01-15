from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from reports.views import imprimir_relatorio

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Autenticação
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Nossas APIs
    path('api/', include('members.urls')),
    path('api/', include('programs.urls')),
    path('api/', include('finances.urls')), # <--- ESSA É A LINHA NOVA!

    # Relatórios
    path('relatorios/imprimir/<int:report_id>/', imprimir_relatorio, name='imprimir_relatorio'),
]