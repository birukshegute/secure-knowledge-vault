from django.contrib.auth.views import LoginView, LogoutView


class UserLoginView(LoginView):
    template_name = "vault/auth/login.html"


class UserLogoutView(LogoutView):
    next_page = "login"