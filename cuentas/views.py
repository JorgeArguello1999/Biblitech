from django.shortcuts import render

# Create your views here.

# This section is for counts on library
def home(request):
    return render(request, "home.html")