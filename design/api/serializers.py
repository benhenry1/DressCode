from rest_framework import serializers
from design.models import (
	DesignLike,
	StatusLike,
	DesignComment,
	StatusComment,
	Design,
	Status,
	DesignShare
)
from account.api.serializers import (
	ProfileSerializer,
	UserSerializer
)


class StatusSerializer(serializers.ModelSerializer):
	profile = ProfileSerializer()
	class Meta:
		model = Status
		fields = [
			'pk',
			'profile',
			'text',
			'timestamp',
		]

class DesignSerializer(serializers.ModelSerializer):
	profile = ProfileSerializer()
	class Meta:
		model = Design
		fields = [
			'pk',
			'profile',
			'title',
			'image',
			'description',
			'timestamp',
		]

class DesignShareSerializer(serializers.ModelSerializer):
	# design = DesignSerializer()
	class Meta:
		model = DesignShare
		fields = [
			'pk',
			'profile',
			'design',
			'timestamp',
		]

class DesignLikeSerializer(serializers.ModelSerializer):
	# design = DesignSerializer()
	class Meta:
		model = DesignLike
		fields = [
			'pk',
			'profile',
			'design',
			'timestamp',
		]

class DesignCommentSerializer(serializers.ModelSerializer):
	# design = DesignSerializer()
	class Meta:
		model = DesignComment
		fields = [
			'pk',
			'profile',
			'design',
			'comment',
			'timestamp',
		]

class StatusLikeSerializer(serializers.ModelSerializer):
	class Meta:
		model = StatusLike
		fields = [
			'pk',
			'profile',
			'status',
			'timestamp',
		]

class StatusCommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = StatusComment
		fields = [
			'pk',
			'profile',
			'status',
			'comment',
			'timestamp',
		]