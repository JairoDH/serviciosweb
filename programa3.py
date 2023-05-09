import requests
import os
import json

#Realiza una consulta del TOP 10 de ESPAÑA 

print("			!! BRAWL STARS !!			")
print("!Búscador sobre jugadores, personajes & mucho más!")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# Solicitar el TAG del jugador
#nombre = input("Ingresa el nombre del personaje(MAYÚS): ")

url_base = f"https://api.brawlstars.com/v1/rankings/es/players?limit=10"
KEY = 'API-KEY'
headers = {'Authorization': KEY}
response = requests.get(url_base, headers=headers)

if response.status_code == 200:
    print("Ranking | Trofeos | Nombre | Tag")
    print("---------------------------------")
    for jugador in response.json()['items']:
        rank = jugador['rank']
        trofeos = jugador['trophies']
        nombre = jugador['name']
        tag = jugador['tag']
        print(f"{rank:<7} | {trofeos:<7} | {nombre:<14} | {tag}")
else:
    print("Error al solicitar los datos del servidor.")

