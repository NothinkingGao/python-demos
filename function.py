#coding:utf-8

#类方法会把类传入
#实例方法
#静态方法,只是一组方法的集合,逻辑上归属某类
#https://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python
def foo(x):
    print "executing foo(%s)"%(x)
 
class A(object):
	def __init__(self,name):
		self.name=name
		self.__superprivate="Hello"
		self._semiprivate=",world!"
		
	def foo(self,x):
	    print "executing foo(%s,%s)"%(self,x)

	@classmethod
	def class_foo2(cls,x):
		print "executing class_foo2:%s"%x

	@classmethod
	def class_foo(cls,x):
		cls.class_foo2('foo2')
		print "executing class_foo(%s,%s)"%(cls,x)

	@staticmethod
	def static_foo(x):
		print "executing static_foo(%s)"%x
 
a=A('kitty')

class Dog(A):
	pass
a.foo('instance method')
A.class_foo('class method')
#A.static_foo('static method')

#Dog.class_foo('dog class method')

#*args和**kwargs

#当你不确定你的函数里将要传递多少参数时你可以用*args.例如,它可以传递任意数量的参数:
def print_everything(*args):
	for count,thing in enumerate(args):
		print '{0}.{1}'.format(count,thing)

print_everything('apple','banana','cabbage')

#**kwargs允许你使用没有事先定义的参数名
def table_things(**kwargs):
	for name,value in kwargs.items():
		print '{0}={1}'.format(name,value)

table_things(apple='fruit',cabbage='vegetable')

#*args和**kwargs可以同时在函数的定义中,但是*args必须在**kwargs前面
