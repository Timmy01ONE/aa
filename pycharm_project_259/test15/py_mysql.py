#!/usr/bin/env python

import pymysql
#创建连接
conn = pymysql.connect(host='10.0.0.66', port=3306, user='root', passwd='123456' , db='test')
#创建游标(位置)
curses = conn.cursor()

effct_row = curses.execute("select * from test2;")

#输出数量
print(effct_row)
#输出第一条数据
print(curses.fetchone())
#取所有
print(curses.fetchall())

#插入数据
data = [
    ("use","passwd")
]

curses.executemany("insert into test2 (aa,bb) values(%s,%s)", data)
#默认开启事务，需要提交
conn.commit()
