from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.


def signupView(req):
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, save)
            return redirect("article:list")
        else:
            return render(req, 'accounts/signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(req, 'accounts/signup.html', {'form': form})


def loginView(req):
    if req.method == 'POST':
        form = AuthenticationForm(data=req.POST)
        if form.is_valid():
            user = form.get_user()
            login(req, user)
            if "next" in req.POST:
                return redirect(req.POST.get("next"))
            return redirect("article:list")
    else:
        form = AuthenticationForm()
    return render(req, 'accounts/login.html', {'form': form})


def logoutView(req):
    if req.method == 'POST':
        logout(req)
    return redirect('article:list')
