"""
Miscellaneous services associated with the web app that aren't
directly accessible by users.
"""
from flask import Blueprint

blueprint = Blueprint('services', __name__)

@blueprint.route('/health')
def health():
    """ A monitoring endpoint which checks to make sure the web server is working. """
    return "Everything is awesome."
