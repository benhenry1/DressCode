from .views import (
	DesignLikeCreateAPIView,
	StatusLikeCreateAPIView,
	StatusCommentCreateAPIView,
	DesignCommentCreateAPIView,
)
 
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('likedesign', DesignLikeCreateAPIView.as_view(), name='like-design'),
	path('likestatus', StatusLikeCreateAPIView.as_view(), name='like-status'),
	path('designcomment', DesignCommentCreateAPIView.as_view(), name='design-comment'),
	path('statuscomment', StatusCommentCreateAPIView.as_view(), name='status-comment'),
]

