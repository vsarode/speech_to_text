#!/bin/bash
export PYTHONPATH=$pwd
#python bishiservice/manage.py makemigrations
#python bishiservice/manage.py migrate
python speech_to_text/conf/service_app.py
