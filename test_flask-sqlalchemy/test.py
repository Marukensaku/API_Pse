#  -*- coding:utf-8 -*-

# 1.连接数据库(配置数据库)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask
import os



basedir = os.path.abspath(os.path.dirname)

#2.描述表结构

# 一个类不能没有构造函数
class User(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),unique=True)
    email = db.Column(db.String(120),unique=True)


    def __init__(self,username,email):
        self.username = username
        self.email = email


    def __repr__(self):
        return '<User %r>' % self.username