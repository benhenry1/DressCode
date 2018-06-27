from rest_framework import generics
from .serializers import (
	DesignLikeSerializer,
	DesignCommentSerializer,
	StatusLikeSerializer,
	StatusCommentSerializer,
	DesignSerializer,
	StatusSerializer,
	DesignShareSerializer
)
from design.models import (
	DesignComment,
	DesignLike,
	StatusComment,
	StatusLike,
	Design,
	Status,
	DesignShare
)

class DesignRetrieveAPIView(generics.RetrieveAPIView):
	lookup_field = 'pk'
	queryset = Design.objects.all()
	serializer_class = DesignSerializer

class DesignCreateAPIView(generics.CreateAPIView):
	lookup_field = 'pk'
	queryset = Design.objects.all()
	serializer_class = DesignSerializer

class StatusCreateAPIView(generics.CreateAPIView):
	lookup_field = 'pk'
	queryset = Status.objects.all()
	serializer_class = StatusSerializer

class DesignShareCreateAPIView(generics.CreateAPIView):
	lookup_field = 'pk'#Still default
	queryset = DesignShare.objects.all();
	serializer_class = DesignShareSerializer

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