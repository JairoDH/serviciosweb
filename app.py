from flask import Flask, render_template, request
import requests

url_base = "https://api.brawlstars.com/v1"
KEY = 'API-KEY'
headers = {'Authorization': KEY}


app = Flask(__name__)

# Función para la ruta principal ("/").
# Retorna el template "inicio.html" al renderizar la página.
@app.route('/')
def inicio():
    return render_template("inicio.html")

# Función para la ruta "/templates/lista.html".
# Obtiene la lista de brawlers de la API y la muestra en el template "lista.html".
@app.route('/templates/lista.html', methods=["GET"])
def listar_brawlers():
    response = requests.get(url_base + "/brawlers", headers=headers)
    brawlers = []
    if response.status_code == 200:
        json = response.json()
        brawlers = json["items"]
        return render_template('lista.html', brawlers=brawlers)
    else:
        return "Error al obtener los detalles del brawler"

# Función para la ruta "/detalles/<brawlerId>".
# Obtiene los detalles de un brawler específico mediante su ID y los muestra en el template "detalles.html".  
@app.route('/detalles/<brawlerId>', methods=["GET"])
def filtrar_brawlers(brawlerId):
    response = requests.get(url_base + f"/brawlers/{brawlerId}", headers=headers)
    if response.status_code == 200:
        brawler = response.json()
        brawlers = [brawler]  # Convertir el brawler en una lista de un solo elemento

        return render_template("detalles.html", brawlers=brawlers)
    else:
        return "Error al obtener los detalles del brawler"
 # Función para que en el html /formulario se recoja la cadena en una variable para utilizar dicha variable como parámetro
 # en la URL en la búsqueda a la API y así permitir solicitud tipo GET.
 
@app.route('/templates/formulario.html', methods=["GET", "POST"])
def formulario():
    if request.method == 'POST':
        return render_template('busqueda.html')
    else:
        return render_template('formulario.html')

# Función para la ruta "/templates/ranking.html".
# Obtiene los rankings global y de España de jugadores desde la API
# y los muestra en el template "ranking.html".   
@app.route('/templates/ranking.html', methods=[ "GET" ])
def ranking():
    response = requests.get(url_base + "/rankings/global/players", headers=headers)
    response1 = requests.get(url_base + "/rankings/es/players", headers=headers)
    if response.status_code and response1.status_code == 200:
        json = response.json()
        json1 = response1.json()
        rank = json["items"][:15] #Limitado a 15 resultados
        rank1 = json1["items"][:15]
        return render_template('ranking.html', rank=rank, rank1=rank1)
    else:
        return "Error al obtener el ranking"
        
# Función en /busqueda.html para que recoja en una variable el contenido del formulario por metodo POST
# y lo utilice para realizar la búsqueda a la API por el metodo GET.    
@app.route('/templates/busqueda.html', methods=["GET", "POST"])
def jugador(): 
    tag = request.form['tag'] #meter en una variable el contenido obtenido del formulario.
    response = requests.get(url_base + f"/players/%23{tag}", headers=headers)
    if response.status_code == 200:
        player = response.json()
        players = [player] 
        return render_template("busqueda.html", players=players)
    else:
        return "Error al obtener los detalles del jugador :" + tag

# Función que recoje en dos response diferentes el ranking GLOBAL y de ESPAÑA, si en ambas peticiones son válidas,
# se recoje en dos variables y los muestra por rakingtpo100.html
@app.route('/templates/rankingtop100.html', methods=[ "GET" ])
def rankingtop100():
    response = requests.get(url_base + "/rankings/global/players", headers=headers)
    response1 = requests.get(url_base + "/rankings/es/players", headers=headers)
    if response.status_code == 200 and response1.status_code == 200:
        json = response.json()
        json1 = response1.json()
        ranktop100 = json["items"][:100] #Limitado a 100 resultados
        ranktop1001 = json1["items"][:100]
        return render_template('rankingtop100.html', ranktop100=ranktop100, ranktop1001=ranktop1001)
    else:
        return "Error al obtener el ranking"        


if __name__ == '__main__':
    app.run("0.0.0.0", 5000, debug=True)
