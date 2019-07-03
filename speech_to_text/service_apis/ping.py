from flask import request
from flask_restful import Resource

# from speech_to_text.utils.resource import BaseResource


class Ping(Resource):
    def get(self):
        query_params = request.args
        print "*************", query_params
        headers = request.headers
        print "--------------->", headers
        return {"Success:": True}

    get.authenticated = False

    def post(self):
        return "hello"
