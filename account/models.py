from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	description = models.TextField(max_length=250, default='')
	city = models.CharField(max_length=50, default='')


#TODO: Nail down Design model
class Design(models.Model):
	user = models.ManyToManyField(User)
	image = models.ImageField()
	description = models.TextField(max_length=250, default='')
	#Add to collecton/playlist/whatever?
	


def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = Profile.objects.create(user=kwargs['instance'])

#Create a profile when a user is created
post_save.connect(create_profile, sender=User)
