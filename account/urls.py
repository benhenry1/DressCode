"""dresscode URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.auth.views import (
    login,
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete
    )
from django.urls import path, include
from account import views

urlpatterns = [
	path('', views.home),

    path('api/', include('account.api.urls')),
    
	path('home/', views.home),
	path('login/', login, {'template_name': 'account/login.html'}),
	path('logout/', views.log_out),
	path('register/', views.register),
    path('change-password/', views.change_password),
    path('reset-password/done', password_reset_done, name="password_reset_done"),
    path('reset-password/confirm/<slug:uidb64><slug:token>',
        password_reset_confirm, name="password_reset_confirm"),
    path('reset-password/complete/', password_reset_complete, name='password_reset_complete'),
    path('reset-password/', password_reset, name="password_reset"),
	path('edit/', views.edit),
    path('<slug:username>/', views.view_profile),
]

