import requests
import logging
from . import mapp # main app/views Blueprint
from flask import render_template, request, redirect, url_for

logging.basicConfig(filename='demo.log', level=logging.DEBUG)

@mapp.route('/', methods=['GET'])
def hello():
    return "hello, world!"

