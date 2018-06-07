from django.shortcuts import (
	render, 
	render_to_response, 
	redirect, get_object_or_404
	)
from django.http import HttpResponse
from design.forms import UploadForm, CommentForm
from django.contrib.auth.models import User
from account.models import Profile
from design.models import Design, DesignComment
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
	return HttpResponse("<h1>Design Home</h1>")

@login_required
def upload(request):
	if request.method == "POST":
		#handle post
		form = UploadForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.profile = Profile.objects.get(user=request.user)
			post.save()
			return redirect('/account')
		else:

			return render(request, 'design/upload.html', {'form': form})
	else:
		form = UploadForm()

		ctxt = {'form': form}
		return render(request, 'design/upload.html', ctxt)

def view_design(request, id):
	design = get_object_or_404(Design, id=id)

	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.profile = Profile.objects.get(user=request.user)
			comment.design = design
			comment.save()

	comments = DesignComment.objects.all().filter(design=design)
	form = CommentForm()
	
	ctxt = {'design': design, 'comments': comments, 'form': form}

	return render(request, 'design/view.html', ctxt)