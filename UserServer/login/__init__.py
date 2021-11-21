from flask import Blueprint

login_bp = Blueprint('login', __name__, url_prefix='/user/login/')

from . import login