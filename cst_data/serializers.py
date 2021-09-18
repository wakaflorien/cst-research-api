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
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = '__all__'


class ModulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modules
        fields = '__all__'
