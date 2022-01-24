from flask import Blueprint

box_bp = Blueprint('box', __name__, url_prefix='/user/box/')

from . import box