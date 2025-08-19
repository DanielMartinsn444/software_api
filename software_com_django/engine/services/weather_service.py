import os
import requests
from engine.services import timezone_service 

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

        
        fuso_horario_data = timezone_service.get_timezone(lat, lon)

      
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
    

def get_weather_by_coords(lat, lon):
    try:
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_KEY}"
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()

        if weather_response.status_code != 200:
            return {"erro": weather_data.get("message", "Erro ao buscar dados de clima.")}

        # Use a função correta: get_timezone
        fuso_horario_data = timezone_service.get_timezone(lat, lon)

        return {
            "servico": "OpenWeather",
            "temperatura": weather_data["main"]["temp"],
            "condicao": weather_data["weather"][0]["description"],
            "cidade": weather_data["name"],
            "pais": weather_data["sys"]["country"],
            "units": "metric",
            "fuso_horario": fuso_horario_data,
        }
    except Exception as e:
        return {"erro": f"Erro inesperado: {str(e)}"}