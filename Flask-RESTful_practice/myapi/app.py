

from flask import Flask
from flask_restful import Api
from resources.foo import Foo
from resources.bar import Bar
from resources.bar import Baz

# Flask核心對象 --->app---->api---->Blueprint ----> 藍圖----->前端、數據庫　　？

app = Flask(__name__)
api = Api(app)

# 靜態路由設置？
api.add_resource(Foo,'/Foo','/Foo/<str:id>')
api.add_resource(Bar,'/Bar','/Bar/<str:id>')
api.add_resource(Baz,'/Baz','/Baz/<str:id>')




