from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FinancialEntryViewSet

router = DefaultRouter()
router.register(r'finances', FinancialEntryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]