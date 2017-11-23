#coding:utf-8

dict={'name':'kitty','age':2}

#默认遍历key
for item in dict:
	print item
#如果只遍历值
for value in dict.values():
	print value

#key和value都遍历
for key,value in dict.items():
	print key,value

#字典转集合(会把key转成集合)
print set(dict)

#字典推导式
d = {key:value for (key, value) in dict.items()}
print d

#例如:快速更换key和value的值
d = {value:key for (key, value) in dict.items()}
print d



