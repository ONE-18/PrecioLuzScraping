from bs4 import BeautifulSoup
import requests

url = 'https://tarifaluzhora.es'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Horas

horasRaw = soup.find_all('div', class_='col-xs-9')

hora = list()

for i in horasRaw:
    hora.append(i.text.split(': '))

horas = list()      # Lista con los intervalos de las horas en el orden original
precio = list()     # Lista con los intervalos de los precios en el orden original
precio1 = list()    # Lista con los intervalos de los precios en orden descendente

cont = 1

for i in hora:
    for j in i:
        if cont % 2 == 0:
            precio.append(j)
            precio1.append(j)
        else:
            horas.append(j)
        cont += 1

precio1.sort(reverse=True)

print('Reducir al máximo el uso de la electricidad en los siguientes tramos:')

for i in precio1:
    if i >= '0.30000 €/kWh':
        print(horas[precio.index(i)] + ':', i)

input()
