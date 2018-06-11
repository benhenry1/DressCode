from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from account.models import Profile
from actstream import action
from notifications.signals import notify

# Create your models here.

'''
Post types. Design and Status
Also handlers which send action signals on create
'''
class Design(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.PROTECT)
	title   = models.CharField(max_length=250, default='')
	image   = models.ImageField(upload_to='designs/')
	description = models.TextField(max_length=500, default='')
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.profile.user) + " " + str(self.timestamp)

	def get_comments(self):
		return DesignComments.objects.get(design=self)

	def num_likes(self):
		return DesignLike.objects.all().count();

	def get_likes(self):
		return DesignLike.objects.all().count();


class Status(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.PROTECT)
	text    = models.TextField(max_length=500, default='')
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.profile.user) + " " + str(self.timestamp)


	def get_comments(self):
		return StatusComments.objects.get(design=self)

	def num_likes(self):
		return StatusLike.objects.all().count();

	def get_likes(self):
		return StatusLike.objects.all().count();


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


'''
Comments: DesignComment and StatusComment. Not DRY code but all I got right now
Also signal handlers that send notifications to owner
'''
class DesignComment(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.PROTECT)
	design  = models.ForeignKey(Design, on_delete=models.CASCADE)
	comment = models.TextField(max_length=500, default='')
	timestamp = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return str(self.profile.user) + " " + str(self.design.title)

class StatusComment(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.PROTECT)
	status  = models.ForeignKey(Status, on_delete=models.CASCADE)
	comment = models.TextField(max_length=250, default='')
	timestamp = models.DateTimeField(auto_now_add=True)

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
		if profile is not status.profile:
			notify.send(profile, recipient=status.profile.user, verb="commented on your status", target=status)
	pass


post_save.connect(statuscomment_notify_handler, sender=StatusComment)


'''
Likes: DesignLike and StatusLike. Still not DRY, still best I got
'''
class DesignLike(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.PROTECT)
	design  = models.ForeignKey(Design, on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=True)

	#If a like from this user already exists,
	#Delete it and don't save the current like
	#Read: Unlike the design
	def save(self, *args, **kwargs):
		try:
			qs = DesignLike.objects.get(profile=self.profile,design=self.design)
			if qs != self:
				qs.delete();
			return;
		except DesignLike.DoesNotExist:
			super().save(*args, **kwargs)
			return;

		#If this is a duplicate like, delete it and returnS
		


class StatusLike(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.PROTECT)
	status  = models.ForeignKey(Status, on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=True)

def designlike_handler(sender, **kwargs):
	if kwargs['created']:
		profile = kwargs['instance'].profile
		design = kwargs['instance'].design
		if profile is not design.profile:
			notify.send(profile, recipient=design.profile.user, verb="liked your design", target=design)
	pass

def statuslike_handler(sender, **kwargs):
	if kwargs['created']:
		profile = kwargs['instance'].profile
		status = kwargs['instance'].status
		if profile is not status.profile:
			notify.send(profile, recipient=status.profile.user, verb="liked your status", target=status)
	pass

post_save.connect(designlike_handler, sender=DesignLike)
post_save.connect(statuslike_handler, sender=StatusLike)