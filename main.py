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

horas = list()
precio = list()
precio1 = list()
cifras = list()
cont = 1

for i in hora:
    for j in i:
        if cont % 2 == 0:
            precio.append(j)
            precio1.append(j)
        else:
            horas.append(j)
        cont += 1

inp = input('Ascendente(a)/Descendente(d): ')

if inp == 'd':
    precio1.sort(reverse=True)
    print('Los tramos con el kWh más caros son:')

elif inp == 'a':
    precio1.sort()
    print('Los tramos con el kWh más baratos son:')

else:
    print('Esa no es una opción')

for i in precio1:
    print(horas[precio.index(i)], 'con un precio de', i)

media = 0

for i in precio1:
    if cont % 2 == 1:
        cifras.append(i.split(' '))
    cont += 1

print(cifras)

# print('Precio medio:', media)
