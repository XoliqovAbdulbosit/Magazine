from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import File


# Create your views here.
def main(request):
    books = File.objects.all()
    return render(request, 'home.html', {'books': books})


def file(request, pk):
    file = File.objects.get(pk=pk)
    return render(request, 'file.html', {'file': file})


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'signin.html', {'error': 'Xato username yoki password'})
    else:
        return render(request, 'signin.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'signup.html', {'errors': form.errors})
    return render(request, 'signup.html')


def signout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
