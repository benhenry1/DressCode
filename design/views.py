from django.shortcuts import (
	render, 
	render_to_response, 
	redirect, get_object_or_404
	)
from django.http import HttpResponse
from design.forms import UploadForm
from django.contrib.auth.models import User
from design.models import Design
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
	return HttpResponse("<h1>Design Home</h1>")

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

			return render(request, 'design/upload.html', {'form': form})
	else:
		form = UploadForm()

		ctxt = {'form': form}
		return render(request, 'design/upload.html', ctxt)