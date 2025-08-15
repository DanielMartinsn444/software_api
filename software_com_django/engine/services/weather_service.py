import os
import requests

API_KEY = os.getenv("OPENWEATHER_KEY")


def get_weather(cidade):
    cidade_formatada = cidade.replace(" ", "%20")
    if not API_KEY:
        return {"erro": "API_KEY não definida"}

    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade_formatada}&appid={API_KEY}&units=metric&lang=pt_br"

    r = requests.get(url)

    if r.status_code != 200:
        return {
            "erro": f"OpenWeather retornou status {r.status_code}",
            "detalhes": r.text,
        }

    data = r.json()

    return {
        "servico": "OpenWeather",
        "temperatura": data["main"]["temp"],
        "condicao": data["weather"][0]["description"],
        "cidade": cidade
    }


res = get_weather("atlanta")
print(res)
