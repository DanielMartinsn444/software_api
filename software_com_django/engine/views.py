from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from engine.services import weather_service

@api_view(['GET'])
def senny_brain(request):
    command = request.query_params.get('cmd')

    if not command:
        return Response({'Erro': "nenhum comando fornecido."}, status=400)

    if command.lower() == "clima":
        cidade = request.query_params.get("cidade", "Belo Horizonte")
        return Response(weather_service.get_weather(cidade))

    return Response({'Erro': "Comando inválido"}, status=400)
