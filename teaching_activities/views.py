from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from research.filter import IsOwnerFilterBackend

class THLIC_CertificateView(viewsets.ModelViewSet):
    serializer_class = THLIC_CertificateSerializer
    permission_classes = [IsAuthenticated]
    queryset = THLIC_Certificate.objects.all()
    filter_backends = [IsOwnerFilterBackend]
   


class Teaching_portofolioView(viewsets.ModelViewSet):
    serializer_class = Teaching_portofolioSerializer
    permission_classes = [IsAuthenticated]
    queryset = Teaching_portofolio.objects.all()
    filter_backends = [IsOwnerFilterBackend]
   
