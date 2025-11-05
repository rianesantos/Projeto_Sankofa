from rest_framework import generics
from .models import Program, Enrollment
from .serializers import ProgramSerializer, EnrollmentSerializer

class ProgramListCreateAPIView(generics.ListCreateAPIView):
    queryset = Program.objects.all().order_by('nome')
    serializer_class = ProgramSerializer
    
class ProgramRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

class EnrollmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Enrollment.objects.all().order_by('-data_inscricao')
    serializer_class = EnrollmentSerializer
    
class EnrollmentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer