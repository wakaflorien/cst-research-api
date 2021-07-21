from .serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


# Create your views here

class College_schoolsView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = College_schools.objects.all()
    serializer_class = College_schoolsSerializer

class Architecture_departmentsView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Architecture_departments.objects.all()
    serializer_class = Architecture_departmentsSerializer

class engineering_departmentsView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = engineering_departments.objects.all()
    serializer_class = engineering_departmentsSerializer

class ict_departmentsView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ict_departments.objects.all()
    serializer_class = ict_departmentsSerializer

class science_departmentsView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = science_departments.objects.all()
    serializer_class = science_departmentsSerializer

class mining_and_geology_departmentsView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = mining_and_geology_departments.objects.all()
    serializer_class = mining_and_geology_departmentsSerializer

class Construction_and_management_modulesView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Construction_and_management_modules.objects.all()
    serializer_class = Construction_and_management_modulesSerializer

class Estate_management_and_valuation_modelsView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Estate_management_and_valuation_models.objects.all()
    serializer_class = Estate_management_and_valuation_modelsSerializer

class Geography_and_urban_planning_modulesView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Geography_and_urban_planning_modules.objects.all()
    serializer_class = Geography_and_urban_planning_modelsSerializer

#-----------------------------------------------------------------------------------------

class Archtecture_moduleslsView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Archtecture_modules.objects.all()
    serializer_class = Archtecture_modulesSerializer

class Electrical_and_Electronics_engineering_modulesView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Electrical_and_Electronics_engineering_modules.objects.all()
    serializer_class = Electrical_and_Electronics_engineering_modulesSerializer

class MEE_modulesView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MEE_modules.objects.all()
    serializer_class = MEE_modulesSerializer

class Civil_environmental_and_geomatic_engineering_modulesView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Civil_environmental_and_geomatic_engineering_modules.objects.all()
    serializer_class = Civil_environmental_and_geomatic_engineering_modulesSerializer

class Computer_and_software_engineering_modulesView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Computer_and_software_engineering_modules.objects.all()
    serializer_class = Computer_and_software_engineering_modulesSerializer


class Information_Technology_modulesView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Information_Technology_modules.objects.all()
    serializer_class = Information_Technology_modulesSerializer

class Information_systems_modulesView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Information_systems_modules.objects.all()
    serializer_class = Information_systems_modulesSerializer

class Computer_sceince_modulesView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Computer_sceince_modules.objects.all()
    serializer_class = Computer_sceince_modulesSerializer

class Information_Technology_modulesView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Information_Technology_modules.objects.all()
    serializer_class = Information_Technology_modulesSerializer

class Biology_modulesView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Biology_modules.objects.all()
    serializer_class = Biology_modulesSerializer

class Chemistry_modulesView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Chemistry_modules.objects.all()
    serializer_class = Chemistry_modulesSerializer

class Mathematics_modulesView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Mathematics_modules.objects.all()
    serializer_class = Mathematics_modulesSerializer

class Physics_modulesView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Physics_modules.objects.all()
    serializer_class = Physics_modulesSerializer

class Geology_modulesView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Geology_modules.objects.all()
    serializer_class = Geology_modulesSerializer

class Mining_modulesView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Mining_modules.objects.all()
    serializer_class = Mining_modulesSerializer
