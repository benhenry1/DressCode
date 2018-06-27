from .views import (
	DesignLikeCreateAPIView,
	StatusLikeCreateAPIView,
	StatusCommentCreateAPIView,
	DesignCommentCreateAPIView,
	DesignCreateAPIView,
	StatusCreateAPIView,
	DesignShareCreateAPIView,
	DesignRetrieveAPIView
)
 
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('view/<int:pk>', DesignRetrieveAPIView.as_view(), name='view-design'),
	path('likedesign', DesignLikeCreateAPIView.as_view(), name='like-design'),
	path('likestatus', StatusLikeCreateAPIView.as_view(), name='like-status'),
	path('designcomment', DesignCommentCreateAPIView.as_view(), name='design-comment'),
	path('statuscomment', StatusCommentCreateAPIView.as_view(), name='status-comment'),
	path('upload', DesignCreateAPIView.as_view(), name='upload-design'),
	path('poststatus', StatusCreateAPIView.as_view(), name='post-status'),
	path('share', DesignShareCreateAPIView.as_view(), name='share'),
]

