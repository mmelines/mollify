import requests
import logging
from . import mapi # api blueprint
from flask import jsonify, session, request

logging.basicConfig(filename='demo.log', level=logging.DEBUG)

@mapi.route('/', methods=['GET'])
def json_hello():
    hello_world = {"message": "hello, world!"}
    return jsonify(hello_world)

