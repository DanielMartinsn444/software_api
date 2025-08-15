from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from engine.services import (
    weather_service,
    price_service,
    quotes_service,
    timezone_service,
    notification_service,
)


@api_view(["GET"])
def senny_brain(request):
    command = request.query_params.get("cmd")

    if not command:
        return Response({"Erro": "nenhum comando fornecido."}, status=400)

    if command.lower() == "clima":
        cidade = request.query_params.get("cidade", "Belo Horizonte")
        return Response(weather_service.get_weather(cidade))

    elif command == "cotacao":

        currency_pair = request.query_params.get("par", "USD-BRL")

        if currency_pair.upper() == "EUR-BRL":
            return Response(price_service.get_price("EUR-BRL"))

    elif command == "fuso-horario":
        cidade = request.query_params.get("cidade")
        regiao = request.query_params.get("regiao")
        if not regiao or not cidade:
            regiao = "America"
            cidade = "Sao_Paulo"
        return Response(timezone_service.get_timezone(regiao, cidade))

    elif command == "mensagem":
        titulo = request.query_params.get("titulo")
        corpo = request.query_params.get("corpo")

        if not titulo:
            titulo = "Notificação padrão"
        if not corpo:
            corpo = "Olá 😃!"

        return Response(notification_service.get_notification(titulo, corpo))

    return Response({"Erro": "Comando inválido"}, status=400)
