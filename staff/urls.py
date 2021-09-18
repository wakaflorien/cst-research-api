from rest_framework import routers
from .views import *
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import path, include

# router = DefaultRouter(trailing_slash=False)
router = SimpleRouter()

router.register(r'profile', ProfileView, basename='profile')
router.register(r'info', CustomStaffView, basename='info')


urlpatterns = router.urls