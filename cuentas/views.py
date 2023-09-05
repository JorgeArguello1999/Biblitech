from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.

# This section is for counts on library
def home(request):
    return render(request, "home.html")

def sigin(request):
    return render(request, "signin.html")

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