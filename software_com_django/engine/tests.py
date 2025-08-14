from django.test import TestCase


import requests

res = requests.get("http://127.0.0.1:8000/api/", params={"cmd": "clima", "cidade": "Belo Horizonte"})
print(res.json())
