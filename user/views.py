from django.shortcuts import render, redirect
from .forms import CustomUserRegisterForm
from django.contrib.auth import logout


def register_user(request):
    if request.method == 'POST':
        form = CustomUserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')
    else:
        form = CustomUserRegisterForm()
    
    return render(request, 'user/register_page.html', {'form':form})



def profile_user(request):
    return render(request, 'user/profile_page.html', {'user':request.user})


def logout_user(request):
    logout(request)
    return redirect('home_page')