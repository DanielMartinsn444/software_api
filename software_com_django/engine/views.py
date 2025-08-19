from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from engine.services import (
    weather_service,
    price_service,
)
from django.contrib.auth import logout
from .models import Usuario
from django.contrib.auth.hashers import make_password, check_password


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = Usuario.objects.get(username=username)
            if check_password(password, user.password):
                request.session["user_id"] = user.id
                return redirect("home")
            else:
                return render(request, "login.html", {"error": "Senha incorreta."})

        except Usuario.DoesNotExist:
            return render(request, "login.html", {"error": "Usuário não encontrado."})

    return render(request, "login.html", {})


def home_view(request):
    if "user_id" not in request.session:
        return redirect("login")
    return render(request, "home.html", {})


def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        if Usuario.objects.filter(email=email).exists():
            return render(
                request, "cadastro.html", {"error": "Este e-mail já está cadastrado."}
            )

        hashed_password = make_password(password)

        Usuario.objects.create(username=username, password=hashed_password, email=email)

        return redirect("login")

    return render(request, "cadastro.html", {})


def logout_view(request):
    logout(request)
    return redirect("login")


@api_view(["GET"])
def senny_brain(request):
    if "user_id" not in request.session:
        return Response(
            {"Erro": "Você precisa estar logado para usar este comando."}, status=403
        )

    command = request.query_params.get("cmd")

    if not command:
        return Response({"Erro": "nenhum comando fornecido."}, status=400)

    match command.lower():
        case "clima":
            cidade = request.query_params.get("cidade")
            if not cidade:
                return Response(
                    {"Erro": "Por favor, forneça uma cidade para o clima."}, status=400
                )
            clima_data = weather_service.get_weather(cidade)
            return Response(clima_data)

        case "cotacao":
            currency_pair = request.query_params.get("par")
            if not currency_pair:
                return Response(
                    {"Erro": "Por favor, forneça um par de moeda para a cotação."},
                    status=400,
                )
            return Response(price_service.get_price(currency_pair))
        case _:
            return Response({"Erro": "Comando inválido"}, status=400)
