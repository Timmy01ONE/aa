#！/usr/bin/env python
import json
f = open("test.text","r")
data = json.loads(f.read())
print(data["name"])