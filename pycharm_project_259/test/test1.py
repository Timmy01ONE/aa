#！/usr/bin/env python
from collections import Iterable    #导入
print(isinstance([],Iterable))     #列表
print(isinstance({},Iterable))     #字典
print(isinstance('abc',Iterable))   #字符串
print(isinstance(10,Iterable))      #数值不行（整数没办法循环）