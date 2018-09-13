# __init__.py 文件的作用是将文件夹变为一个Python模块,Python 中的每个模块的包中，
# 都有__init__.py 文件。
# 通常__init__.py 文件为空，但是我们还可以为它增加其他的功能。我们在导入一个包时
# ，实际上是导入了它的__init__.py文件。
# 这样我们可以在__init__.py文件中批量导入我们所需要的模块，而不再需要一个一个的导入
# （例如api_1_0文件夹下的__init__.py，将其它文件import进来）。
#
# app文件夹下的__init__.py，使用了工厂模式，创建app实例。这样可以创建多个，
# 并且易于被manage.py维护

from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app=app)
    db.init_app(app=app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .api_1 import api_1 as api_blueprint
    app.register_blueprint(api_blueprint)

    return app