from flask import Flask
from flask_restful import Api

from speech_to_text.service_apis.ping import Ping
from speech_to_text.service_apis.speech_to_text import SpeechToText
from speech_to_text.service_apis.upload import Uplaod

app = Flask(__name__)

# App Global varialbls
app.SEND_SMS = False

api = Api(app, prefix='/sttext/')

api.add_resource(Ping, 'ping/')
api.add_resource(Uplaod, 'upload')
api.add_resource(SpeechToText, 'check')

if __name__ == '__main__':
    app.run(host='localhost', port=9002, debug=True)
