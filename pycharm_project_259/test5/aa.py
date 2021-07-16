#!/usr/bin/svn python
class aa:
    def __init__(self,name,ints):
        self.name = name
        self.ints = ints
    def guang(self):
        print("123456")
    def wang(self):
        print(self.name,self.ints)


a = aa(11,22)
a.name = "为啥"
a.wang()
a.guang()
