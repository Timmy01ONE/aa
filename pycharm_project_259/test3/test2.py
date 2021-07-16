#!/usr/bin/env python
import os
os.chdir("c:\\Users")   #切换当前目录到C盘的Users下
print(os.getcwd())
os.chdir(r"d:\python")  #切换当前目录到D盘的python目录下（推荐使用这种方式）
print(os.getcwd())
print(os.curdir)        #返回当前属性
print(os.pardir)        #返回上一级目录
os.makedirs(r"d:\python1")      #递归的创建目录
os.removedirs(r"d:\python1")    #递归的删除目录
os.mkdir(r"d:\python1")         #创建目录
os.rmdir(r"d:\python1")         #删除目录
print(os.listdir(r"d:"))        #输出当前目录的文件
print(os.stat(r"PART6.zip"))    #输出该文件的属性,需要先chdir切换
print(os.sep)       #用于指定不同操作系统的路径分隔符
print(os.linesep)   #用于指定不同操作系统的换行分隔符
print(os.pathsep)   #用户指定不同操作系统的结尾分隔符
print(os.environ)   #查看当前系统的环境变量
print(os.name)      #指当前系统的平台
print(os.system("dir"))     #在当前系统执行该系统的相关命令

print(os.path.abspath(r"PART6.zip"))    #获取该文件的绝对路径
print(os.path.split(r"d:\a\b\c\a.txt")) #将path分割成目录和文件名，分开返回
print(os.path.dirname(r"d:\python1"))   #只取目录名
print(os.path.basename("d:\python1"))   #只取文件名

print(os.path.exists("d:\python1"))     #判断文件是否存在
print(os.path.isabs("d:\python1"))      #判断是否是绝对路径
print(os.path.isfile("python1"))        #判断该文件名是不是文件
print(os.path.isdir("python1"))         #判断该文件名是不是目录
print(os.path.join(r"d:",r"\b"))        #目录拼接

print(os.path.getatime(r"d:\test.txt")) #获得该文件的时间戳
print(os.path.getmtime(r"d:\test.txt")) #获取该文件的修改时间