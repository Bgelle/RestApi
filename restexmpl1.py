from urllib3 import request
#!/usr/bin/env python
# encoding: utf-8
import json
import urllib3
from flask import Flask, jsonify, request
app = Flask(__name__)
@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        data = "hello world"
        return jsonify({'data': data})
app.run()