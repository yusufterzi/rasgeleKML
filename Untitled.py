from flask import Flask,jsonify
from furl import furl
import requests
from flask import request
from gevent.pywsgi import WSGIServer
import resource
from random import randint
import bjoern



resource.setrlimit(resource.RLIMIT_NOFILE, (65536, 65536))
app = Flask(__name__)
headers = {'Content-Type': 'application/json; charset=utf-8'}


@app.route("/getSword")
def getSword():
    return jsonify(rr.json())


if __name__ == '__main__':
    #http_server = WSGIServer(('',300), app)
    #http_server.serve_forever()
    bjoern.run(app, '', int(80))
    #app.run()
