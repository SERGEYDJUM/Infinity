from django.shortcuts import render

def index(reqest):
    return render(reqest,'index.html')

