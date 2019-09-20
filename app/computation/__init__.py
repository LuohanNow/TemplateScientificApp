from flask import Blueprint

bp = Blueprint('computation', __name__)

from app.computation import controller