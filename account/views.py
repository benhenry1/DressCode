from django.shortcuts import (
	render, 
	render_to_response, 
	redirect, get_object_or_404
	)
from django.http import HttpResponse
from account.forms import ( 
	RegistrationForm, 
	EditProfileForm,
	EditPersonalInfoForm,
	)
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django import forms
from account.models import Profile
from design.models import Design
from django.template import RequestContext
from actstream import action
from actstream.models import user_stream, actor_stream
from notifications.models import Notification

# Create your views here.
def index(request):
	return HttpResponse("<h1>This is the index page</h1>")

def login(request):
	if request.user.is_authenticated:
		return redirect('/account/home')

	if request.method == "POST":
		print(request.POST)

	return render(request, 'account/login.html')

def log_out(request):
	logout(request)
	return redirect('/account/login')

@login_required
def home(request):
	try:
		profile = Profile.objects.get(user=request.user)
		posts = Design.objects.all().filter(user=request.user)
		stream = user_stream(request.user, with_user_activity=True)
	except:
		return HttpResponse("<h1>Error: Your account doesn't have a profile</h1>")
		
	if not request.user.is_authenticated or profile is None:
		return redirect('/account/login')

	notifications = request.user.notifications.unread()

	ctxt = {'profile': profile,
			'posts': posts,
			'stream': stream,
			'notifications': notifications}

	return render(request, 'account/home.html', ctxt)

def register(request):
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/account')
		else:
			return render_to_response('account/register.html', {'form': form})
	else:
		form = RegistrationForm()
		ctxt = {'form': form}

		return render(request, 'account/register.html', ctxt)

@login_required
def edit(request):
	#Example of how to get an instance of a model
	profile = get_object_or_404(Profile, user=request.user)

	if request.method == "POST":
		form = EditProfileForm(request.POST, request.FILES, instance=profile)
		infoform = EditPersonalInfoForm(request.POST, instance=profile.user)
		if form.is_valid() and infoform.is_valid():
			form.save()
			infoform.save()
			return redirect('/account')
		else:
			return render_to_response('account/edit.html', {'form': form})
	else:
		form = EditProfileForm(instance=profile)
		infoform = EditPersonalInfoForm(instance=profile.user)
		ctxt = {'user': request.user,
				'form': form,
				'infoform': infoform}

		return render(request, 'account/edit.html', ctxt)


def view_profile(request, username):
	tgt_user = get_object_or_404(User, username=username)
	target = Profile.objects.get(user=tgt_user)
	target_posts = Design.objects.all().filter(user=tgt_user)

	stream = actor_stream(tgt_user)

	ctxt = { 
		'profile': target, 
		'posts': target_posts,
		'stream': stream
	}
	return render(request, 'account/profile.html', ctxt)

@login_required
def change_password(request):
	
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request, user=form.user)
			return redirect('/account')
		else:
			return render(request, 'account/change-password.html', {'form': form})
	else:
		form = PasswordChangeForm(user=request.user)

		ctxt = {'form': form}
		return render(request, "account/change-password.html", ctxt)