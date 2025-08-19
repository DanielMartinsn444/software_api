import requests
import os

API_KEY = os.getenv("TIMEZONEAPIDB_KEY")


def get_timezone(latitude, longitude):
    if not API_KEY:
        return {"erro": "API_KEY não definida"}

    url = "https://api.timezonedb.com/v2.1/get-time-zone"

    params = {
        "key": API_KEY,
        "format": "json",
        "by": "position", 
        "lat": latitude,
        "lng": longitude
    }

    try:
        r = requests.get(url, params=params, timeout=5)
        r.raise_for_status()
        data = r.json()

       
        if data["status"] == "OK":
            return {
                "zona": data["zoneName"],
                "horario": data["formatted"],
                "abrev": data["abbreviation"]
            }
        else:
            return {"erro": f"Não foi possível encontrar o fuso horário. Erro da API: {data.get('message', 'Erro desconhecido')}"}

    except requests.exceptions.Timeout:
        return {"erro": "A requisição para a API demorou demais e foi cancelada."}
    except requests.exceptions.RequestException as e:
        return {"erro": f"Erro ao tentar conectar a API: {e}"}
