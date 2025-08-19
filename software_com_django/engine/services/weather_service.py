import os
import requests
from engine.services.timezone_service import get_timezone 

API_KEY = os.getenv("OPENWEATHER_KEY")

def get_weather(cidade):
    if not API_KEY:
        return {"erro": "API_KEY não definida"}

    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": cidade,
        "appid": API_KEY,
        "units": "metric",
        "lang": "pt_br"
    }

    try:
        r = requests.get(url, params=params)
        r.raise_for_status()
        data = r.json()

        
        lat = data["coord"]["lat"]
        lon = data["coord"]["lon"]

        
        fuso_horario_data = get_timezone(lat, lon)

      
        return {
            "servico": "OpenWeather",
            "temperatura": data["main"]["temp"],
            "condicao": data["weather"][0]["description"],
            "cidade": data["name"],
            "pais": data["sys"]["country"],
            "units": "metric",
            "fuso_horario": fuso_horario_data
        }

    except requests.exceptions.RequestException as e:
        return {"erro": f"Erro na requisição: {e}"}
    except KeyError:
        return {"erro": "Não foi possível encontrar a cidade. Tente novamente."}
    except Exception as e:
        return {"erro": f"Um erro inesperado ocorreu: {e}"}