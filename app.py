from flask import Flask, render_template
import requests, json

url_base = "https://api.brawlstars.com/v1"
KEY = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjI5OGY4NjdmLTg3ZWMtNDA0ZS05ODljLTZkOTQ5OWE1YzUxMCIsImlhdCI6MTY4NTAyOTM3OSwic3ViIjoiZGV2ZWxvcGVyL2Y2MWE1ZDlhLTA1YjEtZGE4My01Nzc2LTkyM2JmYTVjZjU5YyIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiOTAuMTYwLjE0Ni4zNCIsIjkwLjE2MS44Mi4xMjkiXSwidHlwZSI6ImNsaWVudCJ9XX0.BIZrgTG15xHi0FoTJ0r-oS1xvjvCfTLnJk70e66OHvx3Rftzu6cBhZGzoRWagM-SWH3-aamAz1zka4ZQxl6T1A'
headers = {'Authorization': KEY}


app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/templates/lista.html', methods=["GET"])
def listar_brawlers():
    response = requests.get(url_base + "/brawlers", headers=headers)
    brawlers = []
    if response.status_code == 200:
        json = response.json()
        brawlers = json["items"]
    return render_template('lista.html', brawlers=brawlers)
    

@app.route('/detalles/<brawlerId>', methods=["GET"])
def filtrar_brawlers(brawlerId):
    response = requests.get(url_base + f"/brawlers/{brawlerId}", headers=headers)
    if response.status_code == 200:
        brawler = response.json()
        brawlers = [brawler]  # Convertir el brawler en una lista de un solo elemento

        return render_template("detalles.html", brawlers=brawlers)
    else:
        return "Error al obtener los detalles del brawler"


    
    
if __name__ == '__main__':
    app.run("0.0.0.0", 5000, debug=True)
