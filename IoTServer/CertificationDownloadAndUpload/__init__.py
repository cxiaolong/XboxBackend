from flask import Blueprint

certification_bp = Blueprint('certification', __name__)

from . import vpn2_upload
from . import vpn1_download
