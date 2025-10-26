from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import RegisterForm

def register_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(username=name, email=email, password=password)
        user.save()
        login(request, user)
        return redirect('/')
    return render(request, 'register.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Asosiy sahifaga yo‘naltiramiz


        if user.is_superuser:
            return redirect('/secure-admin-2374/')
        elif user.is_staff:
            return redirect('/secure-admin-2374/')
        else:
            return redirect('home')

    else:
        messages.error(request, "email yoki parol xato!")

    return render(request, 'login.html')

