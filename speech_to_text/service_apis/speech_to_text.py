import fnmatch
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


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


class SpeechToText(Resource):
    def post(self):
        # file = request.files['file']
        # if file:
        # filename = secure_filename(file.filename)
        # file.save(os.path.join(UPLOAD_FOLDER, filename))
        files = find('*.wav', UPLOAD_FOLDER)
        response = {}
        for filename in files:
            file = open(os.path.join(UPLOAD_FOLDER, filename))
            response[filename.split('/')[-1]] = get_test_from_speech(file)
        return {"text": response}

    authenticated = False
