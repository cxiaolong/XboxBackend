from flask import Flask
from werkzeug.serving import WSGIRequestHandler

from login import login_bp
from CertificationDownloadAndUpload import certification_bp
from setting import DevelopmentConfig
import logging


def create_flask_app(config):
    """
    创建Flask应用
    :param config: 配置对象
    :return: Flask应用
    """
    app = Flask(__name__)
    app.config.from_object(config)

    app.config.from_envvar("PROJECT_SETTING", silent=True)
    return app


app = create_flask_app(DevelopmentConfig)

app.register_blueprint(login_bp)
app.register_blueprint(certification_bp)

if __name__ == '__main__':
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    handler = logging.FileHandler('flask.log')
    app.logger.addHandler(handler)
    app.run(host="0.0.0.0", port=5000, debug=True)
