from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegistroForm, LoginEmailForm

def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("home")
    else:
        form = RegistroForm()

    return render(request, "Usuarios/registro.html", {"form": form})


def login_email(request):
    if request.method == "POST":
        form = LoginEmailForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            usuario = authenticate(request, email=email, password=password)
            if usuario:
                login(request, usuario)
                return redirect("home")
    else:
        form = LoginEmailForm()
    return render(request, "usuarios/login.html", {"form": form})


def salir(request):
    logout(request)
    return redirect("login")