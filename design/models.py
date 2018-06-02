from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from actstream import action

# Create your models here.
class Design(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='designs/')
	description = models.TextField(max_length=250, default='')
	uploaded_at = models.DateTimeField(auto_now_add=True)
	#Add to collecton/playlist/whatever?

	def __str__(self):
		return str(self.image.url)

#Move to new app
def design_handler(sender, **kwargs):
	if kwargs['created']:
		action.send(kwargs['instance'].user, verb="uploaded a design", target=kwargs['instance'])

#Move to new app
post_save.connect(design_handler, sender=Design)