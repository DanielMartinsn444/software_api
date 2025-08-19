import requests


def get_price(currency_pair):
    url = f"https://economia.awesomeapi.com.br/json/last/{currency_pair}"

    try:
        r = requests.get(url)
        r.raise_for_status()

        data = r.json()

        price_data = data[currency_pair.replace("-", "")]

        return {
            "servico": "AwesomeAPI",
            "par_moedas": f"{price_data['code']}-{price_data['codein']}",
            "nome": price_data["name"],
            "valor_compra": price_data["bid"],
            "valor_venda": price_data["ask"],
            "data_criacao": price_data["create_date"],
        }

    except requests.exceptions.RequestException as e:
        return {"Erro": f"Erro na requisição: {e}"}
    except KeyError:
        return {
            "Erro": f"Par de moedas '{currency_pair}' não encontrado ou formato inválido na resposta."
        }

def get_price_by_coords(lat, lon):
    return get_price("EUR-BRL")