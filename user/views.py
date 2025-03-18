from django.shortcuts import render, redirect
from .forms import CustomUserRegisterForm


def register_user(request):
    if request.method == 'POST':
        form = CustomUserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = CustomUserRegisterForm()
    
    return render(request, 'user/register_page.html', {'form':form})