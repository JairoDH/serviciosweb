#ejercicio 1
#Pedir TAG al jugador y mostrar su nombre con el número de trofeos y el número máximo de trofeos.
import requests
import os
import json

print("			!! BRAWL STARS !!			")
print("!Búscador sobre jugadores, personajes & mucho más!")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# Solicitar el TAG del jugador
TAG = input("Ingresa el TAG del jugador: ")

url_base = f"https://api.brawlstars.com/v1/players/%23{TAG}"
KEY = 'API-KEY'
headers = {'Authorization': KEY}
response = requests.get(url_base, headers=headers)

# Verificar si la solicitud fue correcta y realizar la búsqueda.
if response.status_code == 200:
    json = response.json()
    nombre = json['name']
    Trofeos = json['trophies']
    record_trofeos = json['highestTrophies']
    print(f'El TAG pertenece al jugador {nombre}, tiene actualmente {Trofeos} trofeos y el record de trofeos está en {record_trofeos}')
else:
    # Imprimir un mensaje de error
    print(f"Ha ocurrido un error. Código de estado: {response.status_code}")


