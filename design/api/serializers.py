from rest_framework import serializers
from design.models import DesignLike, StatusLike, DesignComment, StatusComment

class DesignLikeSerializer(serializers.ModelSerializer):
	class Meta:
		model = DesignLike
		fields = [
			'pk',
			'profile',
			'design',
			'timestamp',
		]

class DesignCommentSerializer(serializers.ModelSerializer):
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