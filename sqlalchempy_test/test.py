# -*- coding:utf-8 -*-


# 连接数据库（假定已经有数据库了）
#数据库类型://用户名:密码（没有密码则为空，不填）@数据库主机地址/数据库名?编码
#echo = True 是为了方便 控制台 logging 输出一些sql信息，默认是False
#操作数据库方法1：

#使用 Engine/ConnectionPooling/Dialect 进行数据库操作，Engine使用ConnectionPooling连接数据库，然后再通过Dialect执行SQL语句。
#
#连接数据库使用create_engine():

# from sqlalchemy import create_engine
#
# engine = create_engine('mysql+pymysql://root:123456@localhost/webpy')
#
# #创建表
# engine.execute('create table test1(id int,name varchar(48),salary int not null)')
# #插入表数据
# engine.execute("insert into test1(id,name,salary) values(1,'zs',88888)")
# #查看数据
# result = engine.execute('select * from test1')
# print(result.fetchall())
#

# 操作数据库方法3：

# 使用 ORM/Schema Type/SQL Expression Language/Engine/ConnectionPooling/Dialect 所有组件对数据进行操作。
# 根据类创建对象，对象转换成SQL，执行SQL。


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/28 17:16
# @Author  : Py.qi
# @File    : sqlalchemy_expression.py
# @Software: PyCharm

from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
#echo输出详细
# engine = create_engine("mysql+pymysql://root:123456@localhost/webpy",max_overflow=5,echo=True)
# base=declarative_base() #创建基类
# class user(base):
#     __tablename__ = 'users'
#     id = Column(Integer,primary_key=True,autoincrement=True)
#     hostname=Column(String(64),unique=True,nullable=False)
#     ip_addr=Column(String(56),unique=True,nullable=False)
#     port=Column(Integer,default=22)
#寻找Base的所有子类，按照子类的结构在数据库中生成对应的数据表信息
# base.metadata.create_all(engine)
#
# Session=sessionmaker(bind=engine)
# session=Session()
#增,插入单行
# u = user(hostname='zs',ip_addr='333',port=22)
# session.add(u)
#插入多行
# session.add_all([user(hostname='ls',ip_addr='111',port=873),
#                 user(hostname='ww',ip_addr='888',port=23),
#                 user(hostname='dff',ip_addr='567',port=3306)
#                 ])
#写入数据库
#session.commit()

#删除
#session.query(user).filter(user.id > 3).delete()
#session.commit()

#修改
# session.query(user).filter(user.id == 3).update({'hostname':'feng','port':3389})
# session.commit()

#查
#ret=session.query(user).filter_by(hostname='feng').first()
# ret = session.query(user).filter_by(hostname='feng').all()
# print(ret)

# ret = session.query(user).filter(user.hostname.in_(['sb','bb'])).all()
# print(ret)

# ret = session.query(User.name.label('name_label')).all()
# print(ret,type(ret))

# ret = session.query(User).order_by(User.id).all()
# print(ret)

# ret = session.query(User).order_by(User.id)[1:3]

# print(ret)
# session.commit()


# 操作数据库方法2：

# 使用 Schema Type/SQL Expression Language/Engine/ConnectionPooling/Dialect 进行数据库操作。
# Engine使用Schema Type创建一个特定的结构对象，之后通过SQL Expression Language将该对象转换成SQL语句，
# 然后通过 ConnectionPooling 连接数据库，再然后通过 Dialect 执行SQL，并获取结果。

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/28 16:06
# @Author  : Py.qi
# @File    : sqlalchemy_mysql_metadata.py
# @Software: PyCharm

from sqlalchemy import select,create_engine, Table, Column, Integer, String, MetaData, ForeignKey


#链接数据库
engine = create_engine("mysql+pymysql://root:123456@localhost/webpy", max_overflow=5)
#执行引擎语句
#metadata.create_all(engine)
#获取sql游标
conn = engine.connect()
metadata = MetaData()
#创建表
user = Table('teacher', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(20)),
)
#创建表
color = Table('student', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(20)),
)
# 创建SQL语句，插入数据
sql=user.insert().values(name='aa')
sql1=user.insert().values(name='bb')
#conn.execute(sql)
#conn.close()

#删除数据
#sql3 = user.delete().where(user.c.id > 1)
#conn.execute(sql3)
#conn.close()
#更新数据
#sql4 = user.update().where(user.c.name == 'fenzi').values(name='dddd')
#conn.execute(sql4)
#查询数据
sql5=select([user,])
#sql6 = select([user.c.id,])
#sql7 = select([user.c.id, color.c.name]).where(user.c.id=='6')
# sql = select([user.c.name]).order_by(user.c.name)
# sql = select([user]).group_by(user.c.name)

result = conn.execute(sql5)
print(result.fetchall())
conn.close()