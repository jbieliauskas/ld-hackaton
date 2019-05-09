from flask import Flask, request, Response
import requests
from flask_cors import CORS

app = Flask(__name__) 
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/", methods=['POST'])
def irasyti_mp3():
    url = 'https://liepa.rastija.lt/DesktopModules/LiepasAdmin/TextToSpeech.ashx'
    request_data = request.get_json()
    liepa_response = requests.post(
        url,
        data={
            'text': request_data['text'],
            'voice': '3',
            'speed': '45',
        }
    )
    return '{}/{}.mp3'.format(url, liepa_response.text)

app.run()