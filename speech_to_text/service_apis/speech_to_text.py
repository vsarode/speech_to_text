import fnmatch
import os

import speech_recognition as sr
from flask import request
from flask_restful import Resource

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
    def get(self):
        args = request.args
        file = args['files']
        response = {}
        searched_files = find('*' + file + '*', UPLOAD_FOLDER)
        if searched_files:

            file = open(os.path.join(UPLOAD_FOLDER, searched_files[0]))
            response[searched_files[0].split('/')[-1]] = get_test_from_speech(file)
            return {"text": response}

    get.authenticated = False
