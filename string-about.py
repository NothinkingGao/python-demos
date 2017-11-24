#coding:utf-8
s=""
#删除左边的空格
s.lstrip()
#删除右边的空格
s.rstrip()
#删除两边的空格
s.strip()

#字符串模板
from string import Template
s=Template("Hi,$name! $name is learning $language")
print s.substitute(name="gaoming",language="python")