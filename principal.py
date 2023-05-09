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
KEY = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6Ijk3ZjBiNTBhLWEyMDQtNGU2My05MTRjLTdhNmI4YjBjZDJjNCIsImlhdCI6MTY4MzYxMzc4Miwic3ViIjoiZGV2ZWxvcGVyL2Y2MWE1ZDlhLTA1YjEtZGE4My01Nzc2LTkyM2JmYTVjZjU5YyIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTU4Ljk5LjEuMjQiXSwidHlwZSI6ImNsaWVudCJ9XX0.D0LHA0oEPDBs0QQG7LKntnc1gTYCyQ-xFIE3WXKhNNCc2elxaWovyQotFj2qsKyDdDD5Bz3NyHryeK0IlVl5jw'
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


