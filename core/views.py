from rest_framework import viewsets
from .models import Student, Supervisor, Admin, FieldPlacement
from .serializers import StudentSerializer, SupervisorSerializer, AdminSerializer, FieldPlacementSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class SupervisorViewSet(viewsets.ModelViewSet):
    queryset = Supervisor.objects.all()
    serializer_class = SupervisorSerializer

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class FieldPlacementViewSet(viewsets.ModelViewSet):
    queryset = FieldPlacement.objects.all()
    serializer_class = FieldPlacementSerializer
