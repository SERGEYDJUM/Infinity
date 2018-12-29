from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, Addbook
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.forms import modelformset_factory
from .models import Books
from django.views.decorators.csrf import csrf_exempt


def index(reqest):
    book = Books.objects.all()
    return render(reqest, 'index.html', {'book' : book})

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

@csrf_exempt
def lib(reqest):
    form = Addbook(reqest.POST or None, reqest.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect('/')
    return render(reqest,'lib.html',{'form' : form})

def account(reqest):
    return render(reqest,'account.html')

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')
