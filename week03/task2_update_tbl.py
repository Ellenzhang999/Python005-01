#!/usr/bin/python3

from sqlalchemy.orm import sessionmaker
import mysql
from week3_create_tbl import User_table
from sqlalchemy import create_engine

# 实例一个引擎
dburl = "mysql+pymysql://testuser:testpass@192.168.3.155:3306/testdb?charset=utf8mb4"
engine = create_engine(dburl, echo=True, encoding="utf-8")

# 创建session
SessionClass = sessionmaker(bind=engine)
session = SessionClass()

# 增加数据
user1 = User_table(user_name='Peter')
user2 = User_table(user_name='Kitty')
session.add(user1)
session.add(user2)

# 查询
result = session.query(User_table).all()
for result in session.query(User_table):
    print(result)

session.commit()


