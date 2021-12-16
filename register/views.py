from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from .forms import RegistrationForm
# Create your views here.


def register(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            redirect("main-home")
    context= {"form":form}
    return render(request, "register/register.html",context)
    