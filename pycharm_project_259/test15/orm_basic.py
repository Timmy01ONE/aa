#!/usr/bin/env python
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:123456@10.0.0.66/test",
                       encoding='utf-8',echo=True)

Base = declarative_base()   #生成orm基类

class User(Base):
    __tablename__ = 'test4'  #表名
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

Base.metadata.create_all(engine)   #创建表结构

Session_class = sessionmaker(bind=engine) #创建与数据库的会话session class,注意返回给session的是个class，不是实例
Session = Session_class() #生成session实例

user_obj = User(name='timmy',password='123456') #生成你要创建的数据对象
user_obj1 = User(name='timmy1',password='123456') #生成你要创建的数据对象
print(user_obj.name,user_obj.id) #此时数据还没有创建，打印出来发现id还是none

Session.add(user_obj) #把要创建的对象添加到这个session里面
Session.add(user_obj1) #把要创建的对象添加到这个session里面
print(user_obj.name,user_obj.id) #此时依然还没有创建


Session.commit() #统一提交，创建数据