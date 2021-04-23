from flask import Blueprint

app_one_bp = Blueprint('app_one', __name__)

from app_one import urls
