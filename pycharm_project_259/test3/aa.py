#!/usr/bin/env python
import random
print(random.random())          #随机0-1的浮点数，不能指定区间
print(random.randint(1,3))      #随机1-3的整数
print(random.randrange(1,3))    #随机1-2的整数，不包含3
print(random.choice("hello"))   #从字符串中随机导数一个字符
print(random.choice([1,2,3,4,5]))   #随机输出序列中的一个整数
print(random.sample("hello",3))     #随机取3个字符返回
print(random.uniform(1,10))         #指定区间，随机生成浮点数

number=[1,2,3,4,5,6]       #打乱顺序，洗牌
random.shuffle(number)
print(number)