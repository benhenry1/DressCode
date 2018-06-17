from rest_framework import serializers
from django.contrib.auth.models import User, UserManager
from account.models import Profile


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			'password'
		]

	def create(self, validated_data):
		user = User.objects.create(
			username=validated_data['username'],
			first_name=validated_data['first_name'],
			last_name=validated_data['last_name'],
			email=validated_data['email'],
		)
		user.set_password(validated_data['password'])
		user.save()
		return user

	def update(self, instance, validated_data):
		instance.username = validated_data.get('username', instance.username)
		instance.first_name = validated_data.get('first_name', instance.first_name)
		instance.last_name = validated_data.get('last_name', instance.last_name)
		instance.email = validated_data.get('email', instance.email)
		return instance

class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = [
			'user',
			'image',
			'banner',
			'description',
			'city'
		]