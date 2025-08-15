import requests


def get_quotes():
    url = "https://api.adviceslip.com/advice"

    try:
        r = requests.get(url)
        r.raise_for_status()

        return r.json()
    except requests.exceptions.Timeout:
        return {"erro": "A requisição para a API demorou demais e foi cancelada."}
    except requests.exceptions.RequestException as e:
        return f"{e}"


citacap = get_quotes()
print(citacap)
