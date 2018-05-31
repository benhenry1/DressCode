from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.http import HttpResponse
from account.forms import RegistrationForm, EditProfileForm, UploadForm
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django import forms
from account.models import Profile, Design
from django.template import RequestContext

# Create your views here.
def index(request):
	return HttpResponse("<h1>This is the index page</h1>")

def login(request):
	if request.user.is_authenticated:
		return redirect('/account/home')
	return render(request, 'account/login.html')

def log_out(request):
	logout(request)
	return redirect('/account/login')

@login_required
def home(request):
	profile = Profile.objects.get(user=request.user)
	posts = Design.objects.all().filter(user=request.user)
	if not request.user.is_authenticated:
		return redirect('/account/login')

	ctxt = {'profile': profile,
			'posts': posts}

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
	profile = Profile.objects.get(user=request.user)

	if request.method == "POST":
		form = EditProfileForm(request.POST, instance=profile)
		if form.is_valid():
			form.save()
			return redirect('/account')
		else:
			return render_to_response('account/edit.html', {'form': form})
	else:
		form = EditProfileForm(instance=profile)

		ctxt = {'user': request.user,
				'form': form}

		return render(request, 'account/edit.html', ctxt)


@login_required
def upload(request):
	if request.method == "POST":
		#handle post
		form = UploadForm(request.POST, request.FILES)
		print(request.FILES, request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()
			return redirect('/account')
		else:

			return render(request, 'upload.html', {'form': form})
	else:
		form = UploadForm()

		ctxt = {'form': form}
		return render(request, 'upload.html', ctxt)


def view_profile(request, username):
	tgt_user = get_object_or_404(User, username=username)
	target = Profile.objects.get(user=tgt_user)
	target_posts = Design.objects.all().filter(user=tgt_user)

	ctxt = { 'profile': target, 'posts': target_posts }
	return render(request, 'account/home.html', ctxt)
