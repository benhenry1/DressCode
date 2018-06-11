from rest_framework import generics
from .serializers import DesignLikeSerializer
from design.models import DesignComment, DesignLike, StatusComment, StatusLike

class DesignLikeCreateAPIView(generics.CreateAPIView):
	lookup_field = 'pk' #Default anyway
	queryset = DesignLike.objects.all()
	serializer_class = DesignLikeSerializer
