from django.shortcuts import render

def index(reqest):
    return render(reqest,'index.html')

def signin(reqest):
    return render(reqest,'signin.html')

def login(reqest):
    return render(reqest,'login.html')

def about(reqest):
    return render(reqest,'about.html')

def lib(reqest):
    return render(reqest,'lib.html')

def account(reqest):
    return render(reqest,'account.html')