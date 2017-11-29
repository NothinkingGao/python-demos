#coding:utf-8

mylist=['A','B','C','D','E','A']

#遍历列表
for item in mylist:
	print item

#判断是否可迭代
from collections import Iterable
isinstance(mylist,Iterable)#True

#变成可索引的
for key,value in enumerate(mylist):
	print key,value
# 0 A
# 1 B
# 2 C
# 3 D
# 4 E
#引用两个变量
for x, y in [(1, 1), (2, 4), (3, 9)]:
	print x,y

#list.extend()方法可以追加一组元素进去

aList = [123, 'xyz', 'zara', 'abc', 123];
bList = [2009, 'manni'];
aList.extend(bList)

#删除一个元素
del list[1]

#列表可以直接相加
list1+list2

#判断列表中某个元素的数量
mylist.count('A')#2,里面有两个A

#判断是否在里面
if 'A' in mylist:
	print True

#重复
['Hi!'] * 4

#比较连个列表的元素
cmp(list1,list2)

#返回一个列表中最大的元素
max(mylist)