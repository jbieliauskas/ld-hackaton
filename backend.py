from flask import Flask, request 
import requests
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/synthesizer/transport", methods=['POST'])
def gauti_transporto_mp3(): 
    req_data = request.get_json()
    url = "https://liepa.rastija.lt/DesktopModules/LiepasAdmin/TextToSpeech.ashx"
    transporto_text = req_data['Sablonas'].replace("__Vardas__", req_data['Vardas']).replace("__Suma__", req_data['Suma']).replace("__Numeris__", req_data['Numeris']).replace("__Marke__", req_data['Marke'])
    post_dict = {'text': transporto_text, 'voice': '3', 'speed': '45'}
    post_request = requests.post(url, data = post_dict).text
    get_url = url+"/"+post_request+".mp3"
    get_request = requests.get(get_url)
    return get_url

@app.route("/synthesizer/property", methods=['POST'])
def gauti_turto_mp3(): 
    req_data = request.get_json()
    url = "https://liepa.rastija.lt/DesktopModules/LiepasAdmin/TextToSpeech.ashx"
    turto_text = req_data['Sablonas'].replace("__Vardas__", req_data['Vardas']).replace("__Suma__", req_data['Suma'])
    post_dict = {'text': turto_text, 'voice': '3', 'speed': '45'}
    post_request = requests.post(url, data = post_dict).text
    get_url = url+"/"+post_request+".mp3"
    get_request = requests.get(get_url)
    return get_url
app.run()