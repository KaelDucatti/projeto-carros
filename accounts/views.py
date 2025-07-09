from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


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
