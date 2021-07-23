from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

class THLIC_CertificateView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = THLIC_Certificate.objects.all()
    serializer_class = THLIC_CertificateSerializer


class Teaching_portofolioView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Teaching_portofolio.objects.all()
    serializer_class = Teaching_portofolioSerializer
