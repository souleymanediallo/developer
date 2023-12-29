from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm
from .models import Profile


# Create your views here.
def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html')


def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, 'users/profile.html', context)


def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET.get('next', 'home'))
        else:
            messages.error(request, 'Username OR password is incorrect')

    return render(request, 'users/login.html')


def logoutPage(request):
    logout(request)
    return redirect('home')


def registerUser(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "Account was created for " + user.username)
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, "An error has occurred during registration")

    context = {'form': form}
    return render(request, "users/register.html", context)


@ login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile

    context = {'profile': profile}
    return render(request, "users/account.html", context)