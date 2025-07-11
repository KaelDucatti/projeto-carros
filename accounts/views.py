from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render
from django.views import View


class CreateUserView(View):
    """
    View to handle the creation of a new user.
    """

    def get(self, request):
        form = UserCreationForm()
        return render(
            request, template_name="create_user.html", context={"new_user_form": form}
        )

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        return render(
            request, template_name="create_user.html", context={"new_user_form": form}
        )


class LoginView(View):
    """
    View to handle user login.
    """

    def get(self, request):
        form = AuthenticationForm()
        return render(request, template_name="login.html", context={"login_form": form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("cars_list")
        return render(request, template_name="login.html", context={"login_form": form})


class LogoutView(View):
    """
    View to handle user logout.
    """

    def get(self, request):
        logout(request)
        return redirect("login")
