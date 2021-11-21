from flask import request
from flask import send_from_directory
import os


from . import profile_bp



@profile_bp.route('/CertificationDownloadAndUpload/upload/', methods=['POST'])
# @authentication
def upload():
    f = request.files['upload']
    # base_dir = os.path.dirname(__file__)
    # upload_path = os.path.join(base_dir, 'static/uploads', secure_filename(f.filename))
    # f.save(upload_path)
    f.save('static/file/uploads/file.zip')
    return 'Upload successful'


@profile_bp.route('/CertificationDownloadAndUpload/download/', methods=['GET'])
# @authentication
def download():
    response = send_from_directory(directory='static/file/downloads/', filename='lwg_test_1.ovpn')
    response.headers['my-custom-header'] = 'my-custom-status-0'
    return response


@profile_bp.route('/CertificationDownloadAndUpload/generate_verification/', methods=['GET'])
def generate_verification():
    username = 'cxl'
    try:
        os.system('/OpenVPN/make-openvpn-server.sh -u %s -p -n 10.0.1.0 255.255.255.0' % username)
    except Exception as e:
        print(e)
    return 'OK'