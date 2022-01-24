from flask import Blueprint

vpn_bp = Blueprint('vpn', __name__, url_prefix='/user/vpn/')

from . import vpn

