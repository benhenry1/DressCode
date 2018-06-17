from .views import (
	UserCreateAPIView,
	UserRetrieveUpdateAPIView,
	ProfileRetrieveUpdateAPIView
)
 
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('user/create', UserCreateAPIView.as_view(), name='create-user'),
	path('user/update/<int:pk>', UserRetrieveUpdateAPIView.as_view(), name='update-user'),
	path('profile/update/<int:pk>', ProfileRetrieveUpdateAPIView.as_view(), name='update-profile'),
]

