#coding:utf-8
#默认参数的坑
def add_end_first(L=[]):
	L.append('end')
	return L
print add_end_first()
print add_end_first()
#结果是
# ['end']
# ['end', 'end']
#出现这样结果的原因时函数在定义时默认参数已经被计算出来了
#改成下边这样的就不会有问题
def add_end(L=None):
	if L is None:
		L=[]	
	L.append('end')
	return L

print add_end()
print add_end()