import requests
import json

palabras_wikipedia = [
    "Albert Einstein",
    "La Revolución Francesa",
    "La Teoría de la Relatividad",
    "El ADN",
    "El Universo",
    "La Historia de la Tierra",
    "El Cerebro Humano",
    "La Inteligencia Artificial",
    "El Cambio Climático",
    "La Evolución",
    "La Democracia",
    "La Libertad de Expresión",
    "La Igualdad de Género",
    "Los Derechos Humanos",
    "La Pobreza",
    "El Hambre",
    "La Guerra",
    "La Paz",
    "La Esperanza de Vida",
    "La Salud",
    "La Educación",
    "La Cultura",
    "El Arte",
    "La Literatura",
    "La Música",
    "El Cine",
    "El Teatro",
    "La Danza",
]

url = "https://en.wikipedia.org/w/api.php"
i = 1
for entrada in palabras_wikipedia:
    params = {
        'format': 'json',
        'action': 'query',
        'prop': 'extracts',
        'exintro': '',
        'explaintext': '',
        'redirects': 1,
        'titles': entrada
    }

    req = requests.get(
        url,
        params=params
    ).json()

    n_page = list(req['query']['pages'].keys())[0]
    texto = req['query']['pages'][n_page]['extract']
    texto = '{}<splittername>{}'.format(i, json.dumps(texto))

    if i <= 15:
        with open(f'../1_15/search{i}.txt', 'w') as f:
            f.write(texto)
    else:
        with open(f'../16_30/search{i}.txt', 'w') as f:
            f.write(texto)
    i = i + 1