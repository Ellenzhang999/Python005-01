#!/usr/bin/python3

from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine, Table, Float, Column, Integer, String, MetaData, ForeignKey, Date, CHAR
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy import desc

# 打开数据库连接
Base = declarative_base()

# 用户表：用户 id、用户名、年龄、生日、性别、学历、字段创建时间、字段更新时间
class User_table(Base):
    __tablename__ = 'user'
    user_id = Column(Integer(), primary_key=True)
    user_name = Column(String(50), index=True)
    user_age = Column(Integer())
    user_birth = Column(Date())
    user_sex = Column(CHAR(1))
    user_edu = Column(String(50))
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return "User_table(user_id='{self.user_id}', " \
            "user_name={self.user_name})".format(self=self)

# 实例一个引擎
dburl = "mysql+pymysql://testuser:testpass@192.168.3.155:3306/testdb?charset=utf8mb4"
engine = create_engine(dburl, echo=True, encoding="utf-8")

Base.metadata.create_all(engine)
