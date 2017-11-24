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
 
a=A()

class Dog(A):
	pass
a.foo('instance method')
A.class_foo('class method')
#A.static_foo('static method')

#Dog.class_foo('dog class method')