"""Posts views."""
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from posts.forms import PostForm

# Utilities
from datetime import datetime


posts = [
    {
        'title': 'Traveling!',
        'user': {
            'name': 'Luis Vegas',
            'picture': 'https://picsum.photos/60/60?image=1062'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800?image=1063',
    },
    {
        'title': 'Nice view :-)',
        'user': {
            'name': 'Daniel Lopez',
            'picture': 'https://picsum.photos/60/60?image=823'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800?image=755',
    },
    {
        'title': 'Food!',
        'user': {
            'name': 'Maria Laura',
            'picture': 'https://picsum.photos/60/60?image=836'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800?image=1080',
    }
]

@login_required
def list_posts(request):
    """List existing posts."""
    return render(request, 'posts/feed.html', {'posts': posts})


@login_required   
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("feed")
    else:
        form = PostForm()

    return render(
        request=request,
        template_name = "posts/new.html",
        context ={
            "form":form,
            "user":request.user,
            "profile":request.user.profile
        }
    )