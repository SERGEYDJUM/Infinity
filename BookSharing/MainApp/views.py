from django.shortcuts import render

def index(reqest):
    return render(reqest,'index.html')

def signin(reqest):
    return render(reqest,'signin.html')
