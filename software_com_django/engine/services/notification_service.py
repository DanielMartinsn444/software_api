import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("PUSHBULLETAPI_KEY")


def get_notification(title, body):
    url = "https://api.pushbullet.com/v2/pushes"

    data = {
        "title": title,
        "body": body,
        "type": "note",
    }

    headers = {"Access-Token": API_KEY, "Content-Type": "application/json"}
    try:
        r = requests.post(url, json=data, headers=headers)
        r.raise_for_status()

        return r.json()
    except requests.exceptions.RequestException as e:
        return {"erro": f"erro ao enviar notificação: {e}"}
