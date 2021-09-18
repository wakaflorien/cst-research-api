from django.db.models import fields
from rest_framework import serializers
from rest_framework.permissions import AND
from .models import *

from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse

# from django.shortcuts import render_to_response

class CustomeUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = Staff
        fields = ['email','password','password2',]

        extra_kwargs = {
            'password': {
                'write_only':True
            },
            'password2': {
                'write_only':True
            }
        }
    def save(self):

        user = Staff(
            email=self.validated_data['email'],
            username=self.validated_data['email']
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        email=self.validated_data['email']

        if password != password2:
            raise serializers.ValidationError({'password':'Passwords must match.'})

        if  "ur.ac.rw" not in email:
            raise serializers.ValidationError({"email":"Email Must be UR provided exapmle: yourname@stud.ur.ac.rw!!"})

        user.set_password(password)
        user.save()
        return user

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default = serializers.CurrentUserDefault()
    )
    # owner = serializers.CharField(source ='owner.username', read_only=True)

    class Meta:
        model = Profile
        fields = ['owner','first_name','last_name','gender','specializeArea','school','department','academicRank','appointmentDate',
        'promotionDate','training','responsibilities','teachingWorkload']

        def save(self):

            user = Profile(
            
                owner = self.validated_data['owner'],
                first_name=self.validated_data['first_name'],
                last_name=self.validated_data['last_name'],
                gender=self.validated_data['gender'],
                specializeArea=self.validated_data['specializeArea'],
                school=self.validated_data['school'],
                department=self.validated_data['department'],
                academicRank=self.validated_data['academicRank'],
                appointmentDate=self.validated_data['appointmentDate'],
                promotionDate=self.validated_data['promotionDate'],
                training=self.validated_data['training'],
                responsibilities=self.validated_data['responsibilities'],
                teachingWorkload=self.validated_data['teachingWorkload'],
            )

            # password = self.validated_data['password']
            # password2 = self.validated_data['password2']

            # if password != password2:
            #     raise serializers.ValidationError({'password':'Passwords must match.'})
            # user.set_password(password)
            user.save()
            return user
