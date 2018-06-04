from django.contrib.auth.models import User
from django import forms
from design.models import Design, Comment


class UploadForm(forms.ModelForm):

	class Meta:
		model = Design
		fields = (
			'title',
			'image',
			'description',
		)

	pass

#Unnecessary? Could I just use an <input> and dynamically create the obj? .. yeah probably.
class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = (
			'comment',
		)