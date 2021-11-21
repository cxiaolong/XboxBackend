from flask import Flask
from werkzeug.serving import WSGIRequestHandler

from login import login_bp
from profile import profile_bp
from register import register_bp
from setting import config_dict


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


app = create_flask_app(config_dict.get('dev_config'))

app.register_blueprint(login_bp)
app.register_blueprint(profile_bp)
app.register_blueprint(register_bp)

if __name__ == '__main__':
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(host="39.96.113.207", port="5001", debug=True)
