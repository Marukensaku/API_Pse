# coding:utf-8
import json
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # 显示中文

# 在Flask里 sqlachemy是非常方便的，但是假如数据量很大的话，
# 后台返回的json速度就很慢，很影响用户体验，所以用paginate来分页返回数据paginate(id, num)
#  #id为第几页 num表示一页有几条数据很明显
# 我们的页数应该是 [1,sum/num]所以在前台的页数应该是 1到 数据总数/一页的数据量例如 有7311条数据，
# 我们需要一页10条数据的话页数就是 1 ~ 732 因为还有 最后一页 只有一条数据

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/JS'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

Base = declarative_base()

# sqlalchemy 对已有表做操作需要先做一个映射类

class Js_infos(Base):
    __tablename__ = 'js_infos'
    id = Column(Integer,primary_key=True,nullable=False, autoincrement=True)
    coding = Column(String(11),nullable=True)
    location = Column(String(11),nullable=True)
    name = Column(Text,nullable=True)
    last_price = Column(Text,nullable=True)
    net_value = Column(Text,nullable=True)

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict



# @app.route('/')
# def index():
#     return '<h1>"欢迎来到接口界面"</h1>'



# 这就是纯纯前端的问题了！
@app.route('/')
def index():
    return render_template('chart.html')


# 思考如何把查询的数据变成一个大字典！而不是若干个小字典！
# 从数据库中一次全部查询展示成功
@app.route('/comments', methods=['GET'])
def comments():
    comments = db.session.query(Js_infos.last_price).all()
    t = {}
    t['data'] = comments
    return jsonify(t)

# 关键是前端可以使用的数据格式是什么！　所以前端也要开始　了 也就是前端好不好用！接口有没有用！
    # big_list = {}
    # for item in comments:
    #     big_list.insert(item)
    # return jsonify({'data':big_list})
    # result = []
    # for comment in comments:
    #     result.append(comment.to_json())   # 用到了模型中的转换方法！　映射是成功的！　先做思考分页
    # return jsonify(result), 200





if __name__ == '__main__':
    app.run(debug=True)
