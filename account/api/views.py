from rest_framework import generics
from .serializers import (
	UserSerializer,
	ProfileSerializer,
)
from design.models import Profile
from django.contrib.auth.models import User, UserManager

'''
Create, Retrieve and Update USERs
'''
class UserCreateAPIView(generics.CreateAPIView):
	lookup_field = 'pk' #Default anyway
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
	lookup_field = 'pk'
	queryset = User.objects.all()
	serializer_class = UserSerializer

'''
Retrieve and Update PROFILEs
-- Won't need to create, we have an event handler for that in acct.models
'''
class ProfileRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
	lookup_field = 'pk'
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer