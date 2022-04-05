from django.shortcuts import redirect, render
from .forms import SignUpForm, LoginForm,  UserProfilForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login
from .models import Profile
from django.contrib.auth import update_session_auth_hash




def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SignUpForm
    return render(request, 'signup.html', {'form':form})

def user_login(request):
    if request.method == "POST":
        form = LoginForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('index')
    else:
        form = LoginForm()
    return render(request, "login.html", {'form':form})


def settings(request, username):
    user = Profile.objects.get(username = username)
    if request.method == 'POST':
        form_password = PasswordChangeForm(user=request.user, data=request.POST)
        form = UserProfilForm(request.POST,request.FILES, instance=user)
        if form_password.is_valid():
            form_password.save()
            update_session_auth_hash(request, form_password.user)
            return redirect('profile', username = user.username)
        if form.is_valid():
            form.save()
            return redirect('profile', username = user.username)
    else:
        form = UserProfilForm(instance=user)
        form_password = PasswordChangeForm(user=request.user)
    return render(request, 'settings.html', {'form': form,'form1':form_password})