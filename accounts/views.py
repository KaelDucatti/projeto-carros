from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def new_user_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(
                request,
                template_name="new_user_success.html",
                context={"user_data": form},
            )
    else:
        form = UserCreationForm()
    return render(
        request, template_name="new_user.html", context={"new_user_form": form}
    )
