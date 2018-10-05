# -*- coding:utf-8 -*-
#1. 导入模块
from sqlalchemy import create_engine, String, Integer, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# 2.数据库连接

engine = create_engine("mysql+pymysql://root:123456@localhost/sqlalchemy",
                                    encoding='utf-8', echo=True)

# 3. 创建自定义类，继承基类，自定义类属性中__tablename_
# _这个属性必不可少，代表数据库中表的名字，
# 添加表结构设定一个id属性作为主键，再添加一个name属性。

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    name = Column(String(50))
    addresses = relationship('Address',backref='itsuser')


# uid属性是一个外键，与user表的id关联，
# 记住这里是user表，不是User类，relationship与ForeignKey外键是一起使用的，
# 这样就建立了一对多的关系，user为一，address为多。
# 如果建立的是一对一的关系，只需要在backref参数后面加上uselist=False


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer,primary_key=True)
    uid = Column(Integer,ForeignKey('user.id'))
# 4. 执行创建，将表结构存到了metadata里面，
# 然后让metadata执行create_all()方法，这样就向数据库里创建了user表。


Base.metadata.create_all(engine)

# 5.创建session,之后运行程序进入交互式环境只要操作这个session对象就可以。

Session = sessionmaker(bind=engine)
session = Session()
