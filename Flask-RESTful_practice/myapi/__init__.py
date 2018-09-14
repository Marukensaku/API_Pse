

# 在ａpp(處理app---api的部分)，在ａpp/__init__.py（處理api----->ｂlueprint的部分？）


from flask import Flask,Blueprint
from flask_restful import Api,Resource,url_for


# 把api註冊到藍圖上面？

app = Flask(__name__)
api_bp = Blueprint('api',__name__)
api = Api(api_bp)


class TodoItem(Resource):
    def get(self,id):
        return {'task':'Say "Hello,World!"'}



# 設置好路由之後，再註冊到藍圖上面
api.add_resource(TodoItem,'todos/<int:id>')
app.register_blueprint(api_bp)


