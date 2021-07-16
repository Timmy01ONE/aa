#！/usr/bin/env python
# -*- coding:utf-8  -*-
import json
f = open("tcptwo","rb")
data = json.loads(f.read())
for i in range (0,1000):
    print(i,"、",data["data"][i]["title"])
    for n in range(0,4):
        print(data["data"][i]["options"][n]["oid"], end="")
        print("--->",data["data"][i]["options"][n]["title"])
    print("正确答案：",data["data"][i]["rightoids"],"\n\n\n")