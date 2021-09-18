"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url

from rest_auth.registration.views import VerifyEmailView
from rest_auth.views import PasswordResetView, PasswordResetConfirmView
from allauth.account.views import confirm_email
# from staff.views import ConfirmEmailView

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('staff/', include('staff.urls')),
    path('teaching/', include('teaching_activities.urls')),
    path('', include('research.urls')),
    path('cst/', include('cst_data.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    
    # re_path(r"^account-confirm-email/(?P<key>[-:\w]+)/$", confirm_email, name="account_confirm_email"),
    # url(r'^rest-auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(), name='account_confirm_email'),

    # url(r'^rest-auth/password/reset/$', PasswordResetView.as_view(), name='password_reset'),
    # url(r'^rest-auth/password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    
]