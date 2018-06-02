from django.contrib.auth.models import User
from django import forms
from design.models import Design


class UploadForm(forms.ModelForm):

	class Meta:
		model = Design
		fields = (
			'image',
			'description',
		)

	pass
