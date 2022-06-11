from django.shortcuts import render, redirect

def index(request):
    return redirect('/login')

def login(request):
    return render(request, 'login.html', {})

def register(request):
    return render(request, 'register.html', {})
