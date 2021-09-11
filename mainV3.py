from bs4 import BeautifulSoup
import requests
from numpy import double
import time

url = 'https://tarifaluzhora.es'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

horasRaw = soup.find_all('div', class_='col-xs-9')

hora = list()

for i in horasRaw:
    hora.append(i.text.split(': '))

horas = list()
precio = list()
precioRaw = list()
cont = 1

# Separar Horas y Precios
for i in hora:
    for j in i:
        if cont % 2 == 0:
            precio.append(j)
            precioRaw.append(j)
        else:
            horas.append(j)
        cont += 1

inp = input('Ascendente(a)/Descendente(d): ')

# Descendente

if inp == 'd':
    precioRaw.sort(reverse=True)
    print('\nLos tramos con el kWh más caros son:\n')

# Ascendente

elif inp == 'a':
    precioRaw.sort()
    print('\nLos tramos con el kWh más baratos son:\n')

else:
    print('Esa no es una opción')

for i in precioRaw:
    print(horas[precio.index(i)], 'con un precio de', i)

# Promedio

cifrasRaw = list()
cifras = list()
media = 0
cont = 0

for i in precioRaw:
    cifrasRaw.append(i.split(' '))

for i in cifrasRaw:
    for j in i:
        if cont % 2 == 0:
            cifras.append(j)
        cont += 1

for i in range(0, len(cifras)):
    cifras[i-1] = double(cifras[i-1])
    media += cifras[i-1]

media = media / 24

print('\nPrecio medio:', round(media, 5), '€/kWh')

# Precio instantaneo

Actual = soup.find('span', class_='col-sm-12 sub_text text--center')
Actual = Actual.text.split('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t')

print('\nEl precio a fecha', time.strftime("%d/%m/%y") + ', y hora', time.strftime("%H:%M:%S"), 'es de', Actual[0],
      Actual[1])

input()
