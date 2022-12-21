from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from users.models import CustomUser
from .forms import UserRegisterForm, UserLoginForm


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user = CustomUser.objects.create_user(**form.cleaned_data, is_active=True)
            if user:
                messages.success(request, 'Ви успіщно зареєструвались!')
                return redirect('login')
        else:
            messages.error(request, 'Щось пішло не так!')
        form = UserRegisterForm(request.POST)
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {"form": form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user = authenticate(request, email=request.POST['email'], password=request.POST['password'])
            print(user)
            if user:
                login(request, user)
                return redirect('home')
        form = UserLoginForm(request.POST)
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('home')