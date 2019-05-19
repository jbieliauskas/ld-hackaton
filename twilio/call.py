from flask import Flask, request, make_response
import requests
from flask_cors import CORS
from twilio.rest import Client

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/call", methods=['POST'])
def call():
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)

    request_data = request.get_json()
    url = 'http://9b35dc48.ngrok.io'
    track = request_data['track']
    phone = request_data['phone']
    personId = request_data['personId']

    client.calls.create(
        url='{}/voice?track={}&personId={}'.format(url, track, personId),
        # to='+37062285739',
        to=phone,
        from_='+37052142407'
    )

    return make_response('', 200)

app.run(port=3000)
