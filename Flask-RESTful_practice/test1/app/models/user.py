

from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    # 定义一个属性，默认是读取的操作，这里报错，意思是不可读
    @property
    def password(self):
        raise AttributeError('password is not readable attribute')

    # 定义上面那个password属性的可写属性，这里默认换算成哈希值，然后保存下来
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # 校验传入的密码和哈希值是否是一对儿
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User {}>".format(self.username)