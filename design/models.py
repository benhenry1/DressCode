from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from account.models import Profile
from actstream import action
from notifications.signals import notify

# Create your models here.
class Design(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.PROTECT)
	title = models.CharField(max_length=250, default='')
	image = models.ImageField(upload_to='designs/')
	description = models.TextField(max_length=500, default='')
	uploaded_at = models.DateTimeField(auto_now_add=True)
	#Add to collecton/playlist/whatever?

	def __str__(self):
		return str(self.profile.user) + " " + str(self.uploaded_at)


class Status(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.PROTECT)
	text = models.TextField(max_length=500, default='')
	uploaded_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.profile.user) + " " + str(self.uploaded_at)

def design_handler(sender, **kwargs):
	if kwargs['created']:
		design = kwargs['instance']
		action.send(design.profile.user, verb="uploaded a design", target=design)

post_save.connect(design_handler, sender=Design)

def status_handler(sender, **kwargs):
	if kwargs['created']:
		status = kwargs['instance']
		action.send(status.profile.user, verb="posted a status", target=status)

post_save.connect(status_handler, sender=Status)


class DesignComment(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.PROTECT)
	design = models.ForeignKey(Design, on_delete=models.CASCADE)
	comment = models.TextField(max_length=500, default='')

	def __str__(self):
		return str(self.profile.user) + " " + str(self.design.title)

class StatusComment(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.PROTECT)
	status = models.ForeignKey(Status, on_delete=models.CASCADE)
	comment = models.TextField(max_length=250, default='')

	def __str__(self):
		return str(self.profile.user) + " " + str(self.status.profile.user)


def designcomment_notify_handler(sender, **kwargs):
	if kwargs['created']:
		profile = kwargs['instance'].profile
		design = kwargs['instance'].design
		if sender.profile is not design.profile:
			notify.send(profile, recipient=design.profile.user, verb="commented on your design", target=design)
	pass


post_save.connect(designcomment_notify_handler, sender=DesignComment)

def statuscomment_notify_handler(sender, **kwargs):
	if kwargs['created']:
		profile = kwargs['instance'].profile
		status = kwargs['instance'].status
		if sender.profile is not status.profile:
			notify.send(profile, recipient=status.profile.user, verb="commented on your status", target=status)
	pass


post_save.connect(statuscomment_notify_handler, sender=StatusComment)