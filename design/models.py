from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from actstream import action

# Create your models here.
class Design(models.Model):
	user = models.ForeignKey(User, on_delete=models.PROTECT)
	title = models.TextField(max_length=250, default='')
	image = models.ImageField(upload_to='designs/')
	description = models.TextField(max_length=500, default='')
	uploaded_at = models.DateTimeField(auto_now_add=True)
	#Add to collecton/playlist/whatever?

	def __str__(self):
		return str(self.user.username) + " " + str(self.title)



#Move to new app
def design_handler(sender, **kwargs):
	if kwargs['created']:
		action.send(kwargs['instance'].user, verb="uploaded a design", target=kwargs['instance'])

post_save.connect(design_handler, sender=Design)


class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.PROTECT)
	design = models.ForeignKey(Design, on_delete=models.CASCADE)
	comment = models.TextField(max_length=500, default='')

	def __str__(self):
		return str(self.user.username) + " " + str(self.design.title)

#TODO: Implement notifications
def comment_notify_handler(sender, **kwargs):
	if kwargs['created']:
		user = kwargs['instance'].user
		design = kwargs['instance'].design
		print(str(user.username) + " commented on " + str(design))
	pass


post_save.connect(comment_notify_handler, sender=Comment)