from .views import DesignLikeCreateAPIView
 
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('likedesign', DesignLikeCreateAPIView.as_view(), name='like-design'),
]

