from rest_framework import routers
from .views import *
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import path, include

# router = DefaultRouter(trailing_slash=False)
router = SimpleRouter()

router.register(r'schools', College_schoolsView, basename='cst')
router.register(r'architecture', Architecture_departmentsView, basename='cgfxgh')
router.register(r'engineering', engineering_departmentsView, basename='research')
router.register(r'ict', ict_departmentsView)
router.register(r'science', science_departmentsView, basename='conference')
router.register(r'mining', mining_and_geology_departmentsView, basename='research')
router.register(r'construction/modules', Construction_and_management_modulesView, basename='research')
router.register(r'estate/modules', Estate_management_and_valuation_modelsView, basename='research')
router.register(r'geography_and_urban/modules', Geography_and_urban_planning_modulesView, basename='research')
router.register(r'architecture/modules', Archtecture_moduleslsView, basename='research')
router.register(r'electrical/modules', Electrical_and_Electronics_engineering_modulesView, basename='research')
router.register(r'mee/modules', MEE_modulesView, basename='research')
router.register(r'civil/modules', Civil_environmental_and_geomatic_engineering_modulesView, basename='research')
router.register(r'computer_e/modules', Computer_and_software_engineering_modulesView, basename='research')
router.register(r'it/modules', Information_Technology_modulesView, basename='research')
router.register(r'biology/modules', Biology_modulesView, basename='research')
router.register(r'chemistry/modules', Chemistry_modulesView, basename='research')
router.register(r'mathematics/modules', Mathematics_modulesView, basename='research')
router.register(r'physics/modules', Physics_modulesView, basename='research')
router.register(r'geology/modules', Geology_modulesView, basename='research')
router.register(r'mining/modules/', Mining_modulesView, basename='research')


# urlpatterns = [
#     path('', include(router.urls))
# ]

urlpatterns = router.urls