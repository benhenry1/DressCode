from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from actstream import action

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile_user")
	image = models.ImageField(
		upload_to='profile_pictures/',
		blank=True,
		default="/media/profile_pictures/default.jpg")
	banner = models.ImageField(
		upload_to='profile_banner/',
		 blank=True,
		 default="/media/profile_banner/default.png")
	description = models.TextField(max_length=250, default='')
	city = models.CharField(max_length=50, default='')

	def __str__(self):
		return str(self.user.username)


def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = Profile.objects.create(user=kwargs['instance'])

#Create a profile when a user is created
post_save.connect(create_profile, sender=User)