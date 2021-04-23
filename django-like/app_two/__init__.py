from flask import Blueprint

app_two_bp = Blueprint('app_two', __name__)

from app_two import urls
