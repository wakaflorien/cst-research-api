from rest_framework import routers
from .views import *
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import path, include

# router = DefaultRouter(trailing_slash=False)
router = SimpleRouter()

router.register(r'schools', College_schoolsView, basename='cst')
router.register(r'departments', DepartmentView, basename='cgfxgh')
router.register(r'modules', ModuleView, basename='research')


# urlpatterns = [
#     path('', include(router.urls))
# ]

urlpatterns = router.urls