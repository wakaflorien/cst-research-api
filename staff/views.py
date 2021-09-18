from .serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


# Create your views here

# from rest_auth.registration.views import RegisterView
# from django.contrib.auth import get_user_model
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status

# from rest_framework.exceptions import NotFound
# from rest_framework.views import APIView
# from rest_framework.permissions import AllowAny
# from allauth.account.models import EmailConfirmation, EmailConfirmationHMAC
# from django.http import HttpResponseRedirect


# class ConfirmEmailView(APIView):
#     permission_classes = [AllowAny]

#     def get(self, *args, **kwargs):
#         self.object = confirmation = self.get_object()
#         confirmation.confirm(self.request)
#         # A React Router Route will handle the failure scenario
#         return HttpResponseRedirect('/staff/info/')

#     def get_object(self, queryset=None):
#         key = self.kwargs['key']
#         email_confirmation = EmailConfirmationHMAC.from_key(key)
#         if not email_confirmation:
#             if queryset is None:
#                 queryset = self.get_queryset()
#             try:
#                 email_confirmation = queryset.get(key=key.lower())
#             except EmailConfirmation.DoesNotExist:
#                 # A React Router Route will handle the failure scenario
#                 return HttpResponseRedirect('/login/failure/')
# #         return email_confirmation

#     def get_queryset(self):
#         qs = EmailConfirmation.objects.all_valid()
#         qs = qs.select_related("email_address__user")
#         return qs

class CustomStaffView(viewsets.ModelViewSet):
    serializer_class = CustomeUserSerializer
    # permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        queryset = Staff.objects.filter(email=user)
        return queryset


class ProfileView(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Profile.objects.filter(owner=user)
        return queryset 
    

