from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib import auth
from django.http import HttpResponseRedirect


def index(reqest):
    return render(reqest,'index.html')

def signin(reqest):
    if reqest.method == 'POST':
        form = UserRegisterForm(reqest.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(reqest, f'hi{username}')
            return HttpResponseRedirect('/')
    else:
        form = UserRegisterForm()
    return render(reqest,'registration/signin.html', {'form': form})

def about(reqest):
    return render(reqest,'about.html')

def lib(reqest):
    return render(reqest,'lib.html')

def account(reqest):
    return render(reqest,'account.html')
