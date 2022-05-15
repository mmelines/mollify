from flask import Blueprint

# Blueprint Configuration
mapp = Blueprint(
    'mapp', __name__,
    template_folder = 'templates'
)

from . import main

