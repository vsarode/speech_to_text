import os

import speech_recognition as sr
from flask import request
from flask_restful import Resource
from werkzeug import secure_filename

UPLOAD_FOLDER = '/tmp/'


def get_test_from_speech(file):
    r = sr.Recognizer()
    with sr.AudioFile(file) as source:
        audio = r.record(source)
    try:
        text = r.recognize_google(audio)
    except Exception as e:
        return False
    return text


class SpeechToText(Resource):
    def post(self):
        print "innnnnnnn"
        file = request.files['file']
        import pdb; pdb.set_trace()
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            file = open(os.path.join(UPLOAD_FOLDER, filename))
            res = get_test_from_speech(file)
            print res
            return {"text": res}

    authenticated = False
