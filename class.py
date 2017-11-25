#coding:utf-8

class Person:
    name="aaa"
 
p1=Person()
p2=Person()
p1.name="bbb"
print p1.name  # bbb
print p2.name  # aaa
print Person.name  # aaa

class Person:
    name=[]
 
p1=Person()
p2=Person()
p1.name.append(1)
print p1.name  # [1]
print p2.name  # [1]
print Person.name  # [1]

#创建类
class MyShinyClass(object):
	pass
#或者
#type(类名, 父类的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)
MyShinyClass=type('MyShinyClass',(),{})