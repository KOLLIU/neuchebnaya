from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

# Create your views here.
from users.forms import UserRegisterForm, UserLoginForm


def index(request):
    pass


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Успешная регистрация")
            return redirect("main_page_url")
        else:
            messages.error(request, "Ошибка регистрации")
            context = {"form": form}
    else:
        form = UserRegisterForm()
        context = {"form": form}

    return render(request, "users/register.html", context=context)


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("main_page_url")
        else:
            messages.error(request, "Ошибка авторизации")
            return redirect("main_page_url")
    else:
        form = UserLoginForm()
        context = {"form": form}
    return render(request, "users/login.html", context=context)


def user_logout(request):
    logout(request)
    return redirect("login")
