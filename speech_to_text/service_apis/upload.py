import os

from flask import request
from flask_restful import Resource
from werkzeug import secure_filename

UPLOAD_FOLDER = '/tmp/'


class Uplaod(Resource):
    def post(self):
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return {"success": True}
