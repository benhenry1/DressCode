from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from actstream import action

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='profile_pictures/', blank=True)
	description = models.TextField(max_length=250, default='')
	city = models.CharField(max_length=50, default='')

	def __str__(self):
		return str(self.user.username)


#TODO: Nail down Design model
class Design(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='designs/')
	description = models.TextField(max_length=250, default='')
	uploaded_at = models.DateTimeField(auto_now_add=True)
	#Add to collecton/playlist/whatever?

	def __str__(self):
		return str(self.image.url)




def design_handler(sender, **kwargs):
	if kwargs['created']:
		action.send(kwargs['instance'].user, verb="uploaded a design", target=kwargs['instance'])

#Send activity when design is created by a user
post_save.connect(design_handler, sender=Design)

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = Profile.objects.create(user=kwargs['instance'])

#Create a profile when a user is created
post_save.connect(create_profile, sender=User)