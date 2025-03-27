from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForms, PostFillerForms
from .models import Post
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


def index(request):
    posts = Post.objects.all()
    form = PostFillerForms(request.GET)

    if form.is_valid() and form.cleaned_data['category']:
        posts = posts.filter(category=form.cleaned_data['category'])
        
    print(form.errors)  # Проверим, нет ли ошибок
    print(form.cleaned_data)  # Какие данные приходят?

    return render(request, 'main/home_page.html', {'posts': posts, 'form':form})


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

@login_required
def edit_post(request, id):
    post = get_object_or_404(Post, id=id, author=request.user)

    if request.user == post.author:
        if request.method == 'POST':
            form = PostForms(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('home_page')
        else:
            form = PostForms(instance=post)
    else:
        return HttpResponseForbidden('Вы не автор поста')

    return render(request, 'main/edit_page.html', {'form':form})


def detail_post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'main/detail_page.html', {'post':post})


def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user == post.author:
        post.delete()
        return redirect('home_page')
    else:
        return HttpResponseForbidden('Вы не автор поста')