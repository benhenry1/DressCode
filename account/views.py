from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from account.forms import RegistrationForm, EditProfileForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django import forms
from account.models import Profile

# Create your views here.
def login(request):
	if request.user.is_authenticated:
		return redirect('/account/home')
	return render(request, 'account/login.html')

def log_out(request):
	logout(request)
	return redirect('/account/login')

@login_required
def home(request):
	if not request.user.is_authenticated:
		return redirect('/account/login')

	ctxt = {'user': request.user}

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
