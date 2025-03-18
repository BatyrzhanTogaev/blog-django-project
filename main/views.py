from django.shortcuts import render, redirect
from .forms import PostForms
from .models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'main/home_page.html', {'posts': posts})


def created_post(request):
    if request.method == 'POST':
        form = PostForms(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home_page')
    else:
        form = PostForms()

    return render(request, 'main/create_page.html', {'form':form})
