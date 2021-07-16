#！/usr/bin/env python
# -*- coding:utf-8  -*-
import json

f = open("tca","rb")
data = json.loads(f.read())
for i in range(1,267):
    print(i,"、",data["data"][i]["title"])
    for a in range(0,4):
        print(data["data"][i]["options"][a]["title"])
    print("\n\n\n")
