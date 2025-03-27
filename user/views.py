from django.shortcuts import render, redirect, get_list_or_404
from .forms import CustomUserRegisterForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserform, CustomUserEditForm


def register_user(request):
    if request.method == 'POST':
        form = CustomUserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')
    else:
        form = CustomUserRegisterForm()
    
    return render(request, 'user/register_page.html', {'form':form})


@login_required
def profile_user(request):
    return render(request, 'user/profile_page.html', {'user':request.user})


@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = CustomUserEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile_page')
    else:
        form = CustomUserEditForm(instance=request.user)

    return render(request, 'user/profile_edit.html', {'form':form})


def logout_user(request):
    logout(request)
    return redirect('home_page')