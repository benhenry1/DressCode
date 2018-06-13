from rest_framework import generics
from .serializers import (
	DesignLikeSerializer,
	DesignCommentSerializer,
	StatusLikeSerializer,
	StatusCommentSerializer,
)
from design.models import DesignComment, DesignLike, StatusComment, StatusLike

class DesignLikeCreateAPIView(generics.CreateAPIView):
	lookup_field = 'pk' #Default anyway
	queryset = DesignLike.objects.all()
	serializer_class = DesignLikeSerializer

class DesignCommentCreateAPIView(generics.CreateAPIView):
	lookup_field = 'pk'
	queryset = DesignComment.objects.all()
	serializer_class = DesignCommentSerializer

class StatusLikeCreateAPIView(generics.CreateAPIView):
	lookup_field = 'pk' #Default anyway
	queryset = StatusLike.objects.all()
	serializer_class = StatusLikeSerializer

class StatusCommentCreateAPIView(generics.CreateAPIView):
	lookup_field = 'pk'
	queryset = StatusComment.objects.all()
	serializer_class = StatusCommentSerializer