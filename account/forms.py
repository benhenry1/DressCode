from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import Profile, Design

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2',
		)

	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)

		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']

		if commit:
			user.save()

		return

class EditProfileForm(forms.ModelForm):

	class Meta:
		model = Profile
		fields = (
			'image',
			'city',
			'description',
		)

	pass

class UploadForm(forms.ModelForm):

	class Meta:
		model = Design
		fields = (
			'image',
			'description',
		)

	pass