import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


def partidos(jornada: int):
    response = requests.get(
        f"https://www.quiniela15.com/resultados-quiniela/{jornada}")
    soup = BeautifulSoup(response.content, 'html.parser')
    resultados = soup.find_all(
        class_="is-size-6 is-size-7-mobile has-text-weight-bold")
    lista = []
    for partido in range(0, 28, 2):
        array_res = str(resultados[partido].text) + \
            " - " + str(resultados[partido+1].text)
        lista.append(array_res)
    return lista
