import requests
import os

API_KEY = os.getenv("TIMEZONEAPIDB_KEY")


def get_timezone(regiao, cidade):
    zone_name = f"{regiao}/{cidade}"
    url = f"https://api.timezonedb.com/v2/get-time-zone?key={API_KEY}&format=json&by=zone&zone={zone_name}"

    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.Timeout:
        return {"erro": "A requisição para a API demorou demais e foi cancelada."}
    except requests.exceptions.RequestException as e:
        return {f"Erro ao tentar conectat API: {e}"}


fuso = get_timezone("America", "Sao_Paulo")
print(fuso)
