"""
The `books` blueprint handles displaying recipes.
"""
from flask import Blueprint

books_blueprint = Blueprint('books', __name__, template_folder='templates')

from . import routes
