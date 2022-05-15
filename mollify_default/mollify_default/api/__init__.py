from flask import Blueprint

# Blueprint Configuration
mapi = Blueprint(
    'mapi', __name__,
    template_folder = 'templates'
)

from . import api

