#!/usr/bin/env python
# -*- coding:utf-8  -*-
import json
f = open("test.json","rb")
data = json.loads(f.read())
for i in range (0,1000):
    print("姓名:",data['Data'][i]["Name"])
    print("备注：",data['Data'][i]["Remark"])
    print("电话：",data['Data'][i]["PhoneNum"])
    print("邮箱：",data['Data'][i]["Email"],"\n")