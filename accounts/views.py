from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect


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
        form = AuthenticationForm()
    else:
        form = AuthenticationForm()
    return render(request, template_name="login.html", context={"login_form": form})
