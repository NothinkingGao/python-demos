#coding:utf-8
#python的自省特性

class Dog(object):
	def __init__(self,name,age):
		self.name=name
		self.age=age

	def walk(self):
		print '{0} is walking...'.format(self.name)

dog=Dog(name='kitty',age=3)
#获得对象类型
#print type(dog)

#获取实例化后对象的属性和方法(包括name和age)
print dir(dog)
# ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__',
#  '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', 
#  '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'name', 'walk']

#获取对象的属性和方法(不包括name和age)
print dir(Dog)

#getattr(),hasattr(),isinstance()
print getattr(dog,'name') #kitty
print hasattr(dog,'name') #true
print isinstance(dog,Dog) #true

setattr(dog, 'name', 'jiafeimao')

print getattr(dog,'name')#jiafeimao

#使用inspect模块,帮助使用自省
#is{module|class|function|method|builtin}(obj): 
import inspect

print inspect.getmembers(dog)
print inspect.getmodule(dog)#<module '__main__' from '/home/python/self-know.py'>
#其他的方法再探