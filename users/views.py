from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView

from .forms import SignupForm, LoginForm
from .models import User


class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = "users/signup.html"
    success_url = reverse_lazy("homepage")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class LoginView(DjangoLoginView):
    template_name = "users/login.html"
    authentication_form = LoginForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("homepage")


class LogoutView(DjangoLogoutView):
    next_page = reverse_lazy("users:login")
