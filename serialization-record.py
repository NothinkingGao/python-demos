#coding:utf-8
#序列化python叫Pickle
#cPickle和pickle功能一样，cPickkle是C语言写的，速度快
#pickle是python写的速度慢，优先cPickle
try:
	import cPickle as pickle
except ImportError:
	import pickle

#序列化一个字典
#pickle.dumps()方法把任意对象序列化成一个str
d=dict(name='Bob',age=20,score=88)
result=pickle.dumps(d)
print result

#反序列化
#argument must have 'read' and 'readline' attributes
with open('/home/file','rb') as f:
	obj=pickle.load(result)
	print obj

#序列化为json
#https://docs.python.org/2/library/json.html#json.dumps
import json
class Student(object):
	def __init__(self,name,age,score):
		self.name=name
		self.age=age
		self.score=score
student=Student('Bob',20,88)

#python序列化还需要自己告诉python如何序列化为json,这不合理
def student2dict(std):
	return {
		'name':std.name,
		'age':std.age,
		'score':std.score
	}
print json.dumps(student,default=student2dict)

#可以用这个__dict__,类自带的保存属性和方法的字典
#如果需要特殊序列话的时候可以自己定制
print json.dumps(s, default=lambda obj: obj.__dict__)

#反序列化
#https://docs.python.org/2/library/json.html
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))

#官方这个还是有点不够强大，还是用第三方的库吧Demjson
#https://github.com/dmeranda/demjson