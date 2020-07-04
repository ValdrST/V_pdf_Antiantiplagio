#!/usr/bin/env python
from flask import Flask, escape, request, Blueprint, jsonify, make_response
from os import mkdir, path
import base64
import json
import tempfile
import logging
from .Controller import Controller

server_report = Blueprint('app', __name__)
class Server():
    def __init__(self, name, *args, **kwargs):
        self.app = Flask(name)
        self.app.register_blueprint(server_report)

@server_report.route('/ws/vPdfAntiAntiPlagio',methods=['GET'])
def index():
    return "<h1>vPdfAntiAntiPlagio</h1>"

@server_report.route('/ws/vPdfAntiAntiPlagio/procesar_documento',methods=['POST'])
def procesar_documento():
    print("procesar")
    respuesta = {}
    file = request.files['files[]']
    pdf = file.read()
    pdf_name = file.filename
    f  =  tempfile.TemporaryDirectory()
    file_path = f.name+"/"+pdf_name
    with open(file_path,"wb") as file:
        file.write(pdf)
    try:
        controller = Controller("ws")
        controller.setInputFile(file_path)
        controller.setOutFile(f.name+"/out.pdf")
        controller.setPaginas("")
        controller.save_output()
        with open(f.name+"/out.pdf","rb") as file_out:
            respuesta["datos"] = base64.b64encode(file_out.read()).decode('utf-8')
            respuesta["nombre"] = pdf_name
            response = make_response(json.dumps(respuesta))
            response.headers['Content-Type'] = 'application/json'
            return response, 200
    except Exception:
        logging.error(Exception.mro)
        return "error" , 400

@server_report.route('/ws/vPdfAntiAntiPlagio/procesar_documento',methods=['GET'])
def procesar_documento_get():
    return request.get_json()
    #return "<h1>procesar documento get</h1>"
