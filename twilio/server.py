from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather

app = Flask(__name__)

universal = "https://liepa.rastija.lt/DesktopModules/LiepasAdmin/TextToSpeech.ashx/"

@app.route("/voice", methods=["GET", "POST"])
def voice():
    personId = request.args.get('personId')
    track = request.args.get('track')
    fourUrl = '/four?track={}&personId={}'.format(track, personId)

    resp = VoiceResponse()

    gather = Gather(num_digits=4, action=fourUrl)
    gather.play(universal + 'f17a89fde6dbd258a6bd920eecc166c98c4a22f8-Regina-45.mp3')
    resp.append(gather)

    resp.hangup()

    return str(resp)

@app.route("/four", methods=["GET", "POST"])
def four():
    personId = request.args.get('personId')
    track = request.args.get('track')
    secondUrl = '/second?track={}&personId={}'.format(track, personId)

    resp = VoiceResponse()

    if 'Digits' in request.values:
        choice = request.values['Digits']
        if choice == personId[-4:]:
            resp.redirect(secondUrl)
            return str(resp)
        else:
            resp.play(universal + "55362f11f679b9ea3aadc81543d982695c87f39d-Regina-45.mp3")
            resp.hangup()
    
    resp.hangup()

    return str(resp)

@app.route("/second", methods=["GET", "POST"])
def second():
    personId = request.args.get('personId')
    track = request.args.get('track')
    choicesUrl = '/choices?track={}&personId={}'.format(track, personId)

    resp = VoiceResponse()

    resp.play(track)

    gather = Gather(num_digits=1, action=choicesUrl)
    gather.play(universal + '419f0ae2ec15191b5e23c522ddbc65cda0850f73-Regina-45.mp3')
    resp.append(gather)

    resp.hangup()

    return str(resp)

@app.route("/choices", methods=["GET", "POST"])
def choices():
    personId = request.args.get('personId')
    track = request.args.get('track')
    secondUrl = '/second?track={}&personId={}'.format(track, personId)

    resp = VoiceResponse()

    if 'Digits' in request.values:
        choice = request.values['Digits']
        if choice == '1':
            resp.play(universal + '17c5e8f9a5f48034ffe166772a404ed694bdda71-Regina-45.mp3')
            return str(resp)
        elif choice == '2':
            resp.play(universal + '4e58551171f41679fdfd3ff6c085b805421f0807-Regina-45.mp3')
            return str(resp)
        elif choice == '3':
            resp.redirect(secondUrl)
            return str(resp)
        else:
            resp.play(universal + "55362f11f679b9ea3aadc81543d982695c87f39d-Regina-45.mp3")
            return str(resp)
        
    resp.hangup()

    return str(resp)

app.run(port='7000')
