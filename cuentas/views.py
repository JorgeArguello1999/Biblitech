from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .forms import CountsForm
from .models import Counts
# Create your views here.

# This section is for counts on library
def home(request):
    return render(request, "home.html")

def signin(request):
    if request.method == "GET":
        return render(request, "signin.html", {
            "form": AuthenticationForm 
        })
    else:
        try:
            user = authenticate(
                request,
                username=request.POST["username"],
                password=request.POST["password"]
            )
            if user is None:
                return render(request, "signin.html",{
                    "form": AuthenticationForm,
                    "error": True
                })
            else:
                login(request, user)
                return redirect("home")
        except:
            return redirect("home")

@login_required
def signup(request):
    if request.method == "GET":
        return render(request, "signup.html", {
            "form": UserCreationForm
        })
    else:
        user_information = request.POST
        if user_information['password1'] == user_information['password2']:
            try:
                user = User.objects.create_user(
                    username=user_information["username"],
                    password=user_information["password1"]
                )
                user.save()
                login(request, user)
                return redirect("home")
            except:
                return render(request, "signup.html", {
                    "form": UserCreationForm,
                    "error": True 
                })
        else:
            return render(request, "signup.html", {
                "form": UserCreationForm,
                "error": True 
            })

def signout(request):
    logout(request)
    return redirect("home")

@login_required
def cuentas(request):
    counts = Counts.objects.all()
    return render(request, "cuentas.html", {
        "counts": counts
    })

@login_required
def noticias(request):
    return render(request, "noticias.html", {
        "": ""
    })