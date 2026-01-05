from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.MemberListCreateViewSet.as_view(), name='member-list-create'),
    path('documentos/', views.DocumentoListCreateAPIView.as_view(), name='documento-list-create'),
]
