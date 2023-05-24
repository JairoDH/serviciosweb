from flask import Flask, render_template, request

import requests


url_base = f"https://api.brawlstars.com/v1"
KEY = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6Ijk3ZjBiNTBhLWEyMDQtNGU2My05MTRjLTdhNmI4YjBjZDJjNCIsImlhdCI6MTY4MzYxMzc4Miwic3ViIjoiZGV2ZWxvcGVyL2Y2MWE1ZDlhLTA1YjEtZGE4My01Nzc2LTkyM2JmYTVjZjU5YyIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTU4Ljk5LjEuMjQiXSwidHlwZSI6ImNsaWVudCJ9XX0.D0LHA0oEPDBs0QQG7LKntnc1gTYCyQ-xFIE3WXKhNNCc2elxaWovyQotFj2qsKyDdDD5Bz3NyHryeK0IlVl5jw'
headers = {'Authorization': KEY}
# response = requests.get(url_base+"/brawlers", headers=headers)


app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/juegos', methods = ["GET"])
def juegos():
    response = requests.get(url_base + "/brawlers", headers=headers)

    if response.status_code == 200:
        json_response = response.json()
        brawlers = json_response["items"]

    return render_template('lista.html', brawlers=brawlers)

if __name__ == '__main__':
    app.run("0.0.0.0",5001,debug=True)
