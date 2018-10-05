# 第一种创建表的方式
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String
# # 创建实例，并连接test库
# engine = create_engine("mysql+pymysql://root:123456@localhost/sqlalchemy",
#                                     encoding='utf-8', echo=True)
# # echo=True 显示信息
# Base = declarative_base()  # 生成orm基类
#
# class User(Base):
#     __tablename__ = 'lasuser'  # 表名
#     id = Column(Integer, primary_key=True)
#     name = Column(String(32))
#     password = Column(String(64))
#
# Base.metadata.create_all(engine) #创建表结构 （这里是父类调子类）




 # 另一种创建表的方式



# from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey
# from sqlalchemy.orm import mapper
#
# metadata = MetaData()
#
# user = Table('user', metadata,
#             Column('id', Integer, primary_key=True),
#             Column('name', String(50)),
#             Column('fullname', String(50)),
#             Column('password', String(12))
#         )
#
# class User(object):
#     def __init__(self, name, fullname, password):
#         self.name = name
#         self.fullname = fullname
#         self.password = password
#
# mapper(User, user)  # 类User 和 user关联起来
# # the table metadata is created separately with the Table construct,
# # then associated with the User class via the mapper() function
# # 如果数据库里有，就不会创建了。
from enum import Enum

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
# 创建实例，并连接test库
engine = create_engine("mysql+pymysql://root:123456@localhost/test",
                                    encoding='utf-8', echo=True)

Base = declarative_base()  # 生成orm基类

class Student(Base):
    __tablename__ = 'student'  # 表名
    id = Column(Integer, primary_key=True, autoincrement=True)
    stu_id = Column(Integer)
    age = Column(Integer)  # 整型
    gender = Column(Enum('M','F'),nullable=False)

Base.metadata.create_all(engine) #创建表结构 （这里是父类调子类）

# 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session_class = sessionmaker(bind=engine)
Session = Session_class()  # 生成session实例
stu_obj = Student(stu_id=27, age=22, gender="M")
Session.add(stu_obj)
Session.commit() #现此才统一提交，创建数据