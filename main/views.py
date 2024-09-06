from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import File, Category


# Create your views here.
def main(request):
    books = File.objects.filter(category=Category.objects.get(title='jurnallar'))
    return render(request, 'home.html', {'books': books})


def file(request, pk):
    file = File.objects.get(pk=pk)
    file.views += 1
    file.save()
    return render(request, 'file.html', {'file': file})


def page(request, page):
    books = File.objects.filter(category=Category.objects.get(title=page.lower()))
    query = request.GET.get('query', None)
    if query is not None:
        if query == 'views_asc':
            books = books.order_by('views')
        elif query == 'views_desc':
            books = books.order_by('-views')
        elif query == 'date_asc':
            books = books.order_by('date')
        elif query == 'date_desc':
            books = books.order_by('-date')
    return render(request, 'page.html', {'books': books, 'page': page.capitalize()})


def talab(request):
    return render(request, 'talab.html')


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
