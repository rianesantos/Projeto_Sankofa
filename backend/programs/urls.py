from django.urls import path
from . import views 

urlpatterns = [
    # URLs para Programas
    path('programs/', views.ProgramListCreateAPIView.as_view(), name='program-list-create'),
    path('programs/<int:pk>/', views.ProgramRetrieveUpdateDestroyAPIView.as_view(), name='program-detail'),
    
    # URLs para Inscrições (Enrollments)
    path('enrollments/', views.EnrollmentListCreateAPIView.as_view(), name='enrollment-list-create'),
    path('enrollments/<int:pk>/', views.EnrollmentRetrieveUpdateDestroyAPIView.as_view(), name='enrollment-detail'),
]