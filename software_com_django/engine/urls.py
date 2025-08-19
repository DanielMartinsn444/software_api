# engine/urls.py
from django.urls import path
from .views import home_view, senny_brain, signup_view, logout_view, login_view


urlpatterns = [
    path("", signup_view, name="signup"),
    path("api/", senny_brain, name="senny_dispatcher"),
    path("home/", home_view, name="home"),
    # Rotas de Autenticação
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]
