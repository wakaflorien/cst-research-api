from django.urls import path
from .views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'PRIRC', THLIC_CertificateView, basename='PRIRC')
router.register(r'RPC', Teaching_portofolioView, basename='RPC' )

urlpatterns = router.urls