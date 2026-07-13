from urllib import request
from django.shortcuts import render
from .form import LoginForm, RegisterForm
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout


def logout_view(request):

    logout(request)

    return redirect("home")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST) #creat null form if method is Post


        if form.is_valid(): #django check email , phone ,...
            form.save()
            redirect("login") 

    else:
        form = RegisterForm()

    return render(
                request,
                "register.html",
                {
                "form": form
                }    
            )



def login_view(request):

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            return redirect("home")

    else:

        form = LoginForm()

    return render(
        request,
        "login.html",
        {
            "form": form
        }
    )


def logout_view(request):

    logout(request)

    return redirect("home")
