#!/usr/bin/env python
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:123456@10.0.0.66/test",
                       encoding='utf-8')

Base = declarative_base()   #生成orm基类

class User(Base):
    __tablename__ = 'test4'  #表名
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return "<%s name:%s>" % (self.id,self.name) #返回name


Base.metadata.create_all(engine)   #创建表结构

Session_class = sessionmaker(bind=engine) #创建与数据库的会话session class,注意返回给session的是个class，不是实例
Session = Session_class() #生成session实例


data = Session.query(User).filter(User.id >1).filter(User.id <4).first()
print(data)

# data.name = "timmy_one"
# data.password = "timmy_test"
# Session.commit()