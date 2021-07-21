from django.shortcuts import redirect
from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *

class College_schoolsSerializer(serializers.ModelSerializer):
    # arcdepartments = serializers.StringRelatedField(many=True, source='', read_only=True)
    # engdepartments = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = College_schools
        fields = ['school_code','school_name']

class Architecture_departmentsSerializer(serializers.ModelSerializer):
    arcmodules =serializers.StringRelatedField(many=True)
    class Meta:
        model = Architecture_departments
        fields = '__all__'


class engineering_departmentsSerializer(serializers.ModelSerializer):
    engmodules =serializers.StringRelatedField(many=True)
    class Meta:
        model = engineering_departments
        fields = '__all__'

class ict_departmentsSerializer(serializers.ModelSerializer):
    ictmodules =serializers.StringRelatedField(many=True)
    class Meta:
        model = ict_departments
        fields = '__all__'

class science_departmentsSerializer(serializers.ModelSerializer):
    sciemodules =serializers.StringRelatedField(many=True)
    class Meta:
        model = science_departments
        fields = '__all__'

class mining_and_geology_departmentsSerializer(serializers.ModelSerializer):
    minmodules =serializers.StringRelatedField(many=True)
    class Meta:
        model = mining_and_geology_departments
        fields = '__all__'

class Construction_and_management_modulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Construction_and_management_modules
        fields = '__all__'


class Estate_management_and_valuation_modelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estate_management_and_valuation_models
        fields = '__all__'

class Geography_and_urban_planning_modelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geography_and_urban_planning_modules
        fields = '__all__'

class Archtecture_modulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archtecture_modules
        fields = '__all__'

class Electrical_and_Electronics_engineering_modulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Electrical_and_Electronics_engineering_modules
        fields = '__all__'

class MEE_modulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MEE_modules
        fields = '__all__'

class Civil_environmental_and_geomatic_engineering_modulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_environmental_and_geomatic_engineering_modules
        fields = '__all__'

class Computer_and_software_engineering_modulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computer_and_software_engineering_modules
        fields = '__all__'

class Information_Technology_modulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information_Technology_modules
        fields = '__all__'

class Information_systems_modulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information_systems_modules
        fields = '__all__'

class Computer_sceince_modulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computer_sceince_modules
        fields = '__all__'

class Biology_modulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biology_modules
        fields = '__all__'

class Chemistry_modulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chemistry_modules
        fields = '__all__'

class Mathematics_modulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mathematics_modules
        fields = '__all__'

class Physics_modulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Physics_modules
        fields = '__all__'

class Geology_modulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geology_modules
        fields = '__all__'

class Mining_modulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mining_modules
        fields = '__all__'
