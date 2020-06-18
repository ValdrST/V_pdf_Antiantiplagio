#!/usr/bin/env python
from flask import Flask, escape, request, Blueprint, jsonify, make_response
from os import mkdir, path
import base64
import json

server_report = Blueprint('app', __name__)
class Server():
    def __init__(self, name, *args, **kwargs):
        self.app = Flask(name)
        self.app.register_blueprint(server_report)

@server_report.route('/',methods=['GET'])
def index():
    return "<h1>vPdfAntiAntiPlagio</h1>"