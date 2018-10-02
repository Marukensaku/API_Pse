
# 引入上下文
from flask import Flask, config
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from conf


app = Flask(__name__)
app.config.from_object(config)


db = SQLAlchemy(app)
manager = Manager(app)

def create_app():
    app = Flask(__name__)
    db.init_app(app)
    return app


#在脚本里面使用 with 声明都样也有作用:
# def my_function():
#     with app.app_context():
#         user = db.User(...)
#         db.session.add(user)
#         db.session.commit()


if __name__ == "__main__":
    manager.run()