from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config
from flask_script import Manager



# 还是要有创建的套路！
app = Flask(__name__)
app.config.from_object(config)






db = SQLAlchemy(app)  # 初始化一个对象

manager = Manager(app)

# 声明模型
# 简单模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    addresses = db.relationship('Address',
        backref=db.backref('person', lazy='joined'), lazy='dynamic')
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username
# 一对多 模型

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    addresses = db.relationship('Address', backref='person',
                                lazy='dynamic')

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))


# 多对多模型
tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('page_id', db.Integer, db.ForeignKey('page.id'))
)

class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tags = db.relationship('Tag', secondary=tags,
        backref=db.backref('pages', lazy='dynamic'))

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)


# 选择（select）,插入（insert）,删除（delete）

# 向数据库插入数据分为三个步骤:
#
# 创建 Python 对象
# 把它添加到会话
# 提交会话

# 删除记录
# 删除记录是十分类似的，使用 delete() 代替 add():
#
# >>> db.session.delete(me)
# >>> db.session.commit()

# 查询记录
# 那么我们怎么从数据库中查询数据？
# 为此，Flask-SQLAlchemy 在您的 Model 类上提供了 query 属性。
# 当您访问它时，您会得到一个新的所有记录的查询对象。在使用 all()
# 或者 first() 发起查询之前可以使用方法 filter() 来过滤记录。
# 如果您想要用主键查询的话，也可以使用 get()。

#
# 在视图中查询
# 当您编写 Flask 视图函数，对于不存在的条目返回一个 404 错误是非常方便的。
# 因为这是一个很常见的问题，Flask-SQLAlchemy 为了解决这个问题提供了一个帮助函数。
# 可以使用 get_or_404() 来代替 get()，使用 first_or_404() 来代替 first()。这样会抛出一个 404 错误，而不是返回 None:
#
# @app.route('/user/<username>')
# def show_user(username):
#     user = User.query.filter_by(username=username).first_or_404()
#     return render_template('show_user.html', user=user)