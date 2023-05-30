
#Pedir nombre del personaje y mostrar información
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
id = input("Ingresa el ID del personaje): ")

url_base = f"https://api.brawlstars.com/v1/brawlers/{id}"
KEY = 'API-KEY'
headers = {'Authorization': KEY}
response = requests.get(url_base, headers=headers)

if response.status_code == 200:
    json = response.json()
    name = json["name"]
    starPowers = json["starPowers"]
    gadgets = json["gadgets"]

    print(f"Estas son las Star Powers y los gadgets de {name}:")
    print("Los poderes son :") 
    for starPower in starPowers:
        print(starPower["name"])
    print("Los gadgets son:")
    for var in gadgets:
        print(var["name"])
    
else:
    print("Ha ocurrido un error. Código de estado:", response.status_code)

