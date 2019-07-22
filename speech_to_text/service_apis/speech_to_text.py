import glob

import speech_recognition as sr
from flask import request
from flask_restful import Resource

# UPLOAD_FOLDER = 'F:\\uploadFolder\\' #os.path.join("F:", "uploadFolder")


fileName = ""
files = ""
data = []
fdata = ""
fnamelist = []
speech_to_text = {}
UPLOAD_FOLDER = '/tmp/uploadFolder/'  # os.path.join("F:", "uploadFolder")


def printit(filterfile=""):
    global fdata
    global strdata
    strdata = ""
    fdata = ""
    text = ""
    global speech_to_text
    # threading.Timer(10.0, printit).start()
    filenames = glob.glob(UPLOAD_FOLDER + "*.wav")
    # print(filenames)
    if (len(filenames) > 0):
        for index in range(len(filenames)):
            fileName = filenames[index]
            fpathlist = fileName.split("/")
            files = fpathlist[len(fpathlist) - 1]
            fnamelist = files.split("_")
            if (filterfile in files):
                fdata = fdata + files + ":"
                r = sr.Recognizer()
                audio =  UPLOAD_FOLDER+files
                with sr.AudioFile(audio) as source:
                    audio = r.record(source)
                try:
                    text = r.recognize_google(audio)
                    speech_to_text[files] = text
                except Exception as e:
                    print(e)
                data.append(text + ":")
                strdata = strdata + text + ":"
        f = open(UPLOAD_FOLDER + filterfile + ".txt", "w")
        f.writelines(data)
        f.close()
        # return data
        return strdata + "@" + fdata
        # print(speech_to_text)
        # print(strdata + "@" + fdata)
    else:
        print("file not uploaded")


class SpeechToText(Resource):
    def post(self):
        args = request.args
        files = args['files']
        responseFinal = printit(files)
        return responseFinal
