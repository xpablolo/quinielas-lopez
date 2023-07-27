import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

dicc = {"Óscar": 0, "Pablo": 1, "Fernando": 2, "Martín": 3, "María": 4, "Carlos": 5,
        "Jorge": 6, "Clara": 7, "Abuela": 8, "Nuria": 9, "Anita": 10}
dicc2 = {0: "Óscar", 1: "Pablo", 2: "Fernando", 3: "Martín", 4: "María", 5: "Carlos",
         6: "Jorge", 7: "Clara", 8: "Abuela", 9: "Nuria", 10: "Anita"}


def give_array_res(jornada):
    response = requests.get(
        f"https://www.quiniela15.com/resultados-quiniela/{jornada}")
    soup = BeautifulSoup(response.content, 'html.parser')
    resultados = soup.find_all(
        class_="is-vertical-center has-text-centered is-size-5 is-size-6-mobile")
    array_res = ""
    for partido in range(14):
        array_res = array_res + str(resultados[partido].text[2])
    return array_res


def give_array_jornadas(path):
    dataframe = pd.read_excel(path, usecols=[0])
    lista = dataframe.values
    lista = lista.flatten().tolist()
    return list(map(int, lista))


dataframe1 = pd.read_excel('datos.xlsx')
lista_values = dataframe1.values
# print(lista_values[-1])


def aciertos(resultados, lista):
    list_aciertos = []
    for index in range(1, len(lista)):
        prediction, aciertos = lista[index], 0
        if type(prediction) == type(0.1):
            list_aciertos.append("-")
            continue
        elif len(str(prediction)) != 14:
            list_aciertos.append("w.")
            continue
        prediction = list(str(prediction))
        for index2 in range(len(resultados)):
            if prediction[index2] == "x":
                prediction[index2] = "X"
            if resultados[index2] == prediction[index2]:
                aciertos += 1
        list_aciertos.append(aciertos)
    return list_aciertos


list_jornadas = give_array_jornadas("datos.xlsx")
lista_def = []

for jornada in list_jornadas:
    resultados = give_array_res(jornada)
    lista_aciertos = aciertos(
        resultados, lista_values[list_jornadas.index(jornada)])
    lista_def.append(lista_aciertos)

list_jornadas = ['J. {0}'.format(element) for element in list_jornadas]
list_jornadas.append("Promedio")
list_jornadas.append("Máx.")


def remove_values_from_list(the_list, val):
    return [value for value in the_list if value != val]


np_list = np.array(lista_def)
promedio, max_l = [], []
for i in range(len(lista_def[0])):
    aciertos = np_list[:, i].tolist()
    aciertos = remove_values_from_list(aciertos, '-')
    aciertos = remove_values_from_list(aciertos, 'w.')
    aciertos = list(map(int, aciertos))
    promedio.append(round(sum(aciertos)/len(aciertos), 2))
    max_l.append(max(aciertos))
lista_def.append(promedio)
lista_def.append(max_l)

df = pd.DataFrame(lista_def,
                  index=list_jornadas, columns=list(dicc.keys()))
df.to_excel('Resultados.xlsx', sheet_name="2022-23")
