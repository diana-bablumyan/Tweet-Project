from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import UserLoginForm, ProfileUpdateForm
from to_do.models import NewTweet
from django.contrib import messages
from to_do.views import retrieve_tweet


def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    context = {'form': form}
    return render(request, 'users/register.html', context)


def user_login(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.info(request, 'If you registered now, Update your page in advance please!')
                return redirect('home')
            else:
                return redirect('user_login')
    else:
        return render(request, 'users/user_login.html', {'form': form})


@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('home')


@login_required
def profile_view(request, user_id):
    if request.user.id != user_id:
        return HttpResponse("It's not your profile, you can't open that!")
    profile = Profile.objects.get(user_id=user_id)
    tweet_list = NewTweet.objects.all()
    return render(request, "users/profile.html", {'profile': profile, 'tweet_list': tweet_list})

@login_required
def update_profile(request, profile_id):
    if request.user.profile.id != profile_id:
        return HttpResponse("It's not your profile, you can't update that!")

    profile = Profile.objects.get(id=profile_id)
    form = ProfileUpdateForm(instance=profile)
    if request.method == 'POST':
        form = ProfileUpdateForm(instance=profile, data=request.POST)
        if form.is_valid():
            form.save()
            if request.FILES.get('profile_image', None) != None:
                profile.profile_image = request.FILES['profile_image']
                profile.save()
            return redirect('profile', user_id=profile.user.id)

    return render(request, "users/update_profile.html", {'form': form})
