from flask import Blueprint

profile_bp = Blueprint('CertificationDownloadAndUpload', __name__)

from . import profile
