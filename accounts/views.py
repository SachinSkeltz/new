from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account is created for ' + user + ', Please login')
                return redirect('login')
        context = {'form': form}
        return render(request, 'register.html', context)


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        usr_nm = None
        pswd = None

        if request.method == "POST":
            usr_nm = request.POST.get('username')
            pswd = request.POST.get('password')

        user = authenticate(request, username=usr_nm, password=pswd)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Please enter valid Username & Password')

        context = {}
        return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return render(request, 'login.html')
