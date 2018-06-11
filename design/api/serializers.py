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