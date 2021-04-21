from django.shortcuts import render

# Create your views here.
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


def default_EnterCredentials_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        if authenticate(username=username, password=password) is not None:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    print("User Authenticated")
                    return redirect("item/list")
    context = {
        "form": form
    }
    return render(request, "login/preCredentials.html", context)


def noValidCredentials_view(request):
    return render(request, "login/InvalidCredentialsOrSession.html", context={})