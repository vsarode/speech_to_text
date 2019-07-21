import os

from flask import request
from flask_restful import Resource
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/tmp/uploadFolder' #os.path.join("F:", "uploadFolder")


class Uplaod(Resource):
    def post(self):
        file = request.files['image']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return {"message": True}
