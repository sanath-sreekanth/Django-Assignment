from django.shortcuts import render, redirect
from .models import User, Post
from .forms import PostForm

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_created')
        pass
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

def post_created(request):
    return render(request, 'post_created.html')
