#coding:utf-8

#open a file
f=open('/home/file.txt')
f.open()
f.close()

#try..catch..finally
try:
	f=open('/home/file.txt',r)
	print f.read()
finally:
	if f:
		f.close()

#with open a file
with open('/home/file.txt','r') as f:
	print f.read()
#read by line
with open('/home/file.txt','r') as f:
	for line in f.readlines():
		print line.strip()
#read by binary
f=open('/home/test.jpg','rb')
f.read()

#read and decode
f.read().decode('gbk')

#write a file
f=open('/home/file.txt','w')
f.write('hello,world')
f.close()

#or 
with open('/home/file.txt') as f:
	f.write('Hello,world')