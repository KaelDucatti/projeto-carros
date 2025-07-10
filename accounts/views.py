from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render


def new_user_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(
        request, template_name="new_user.html", context={"new_user_form": form}
    )


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("cars_list")
    else:
        form = AuthenticationForm()
    return render(request, template_name="login.html", context={"login_form": form})


def logout_view(request):
    logout(request)
    return redirect("login")
