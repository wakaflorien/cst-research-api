from .serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


# Create your views here

class College_schoolsView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = College_schools.objects.all()
    serializer_class = College_schoolsSerializer


class DepartmentView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer

class ModuleView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Modules.objects.all()
    serializer_class = ModulesSerializer
