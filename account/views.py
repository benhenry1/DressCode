from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from account.forms import RegistrationForm

# Create your views here.
def login(request):
	if request.user.is_authenticated:
		return redirect('/account')
	return render(request, 'account/login.html')

def home(request):
	if not request.user.is_authenticated:
		return redirect('/account/login')

	ctxt = {'user': request.user}

	return render(request, 'account/home.html', ctxt)

def register(request):
	if request.method == "POST":
		#Handle form submission
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
