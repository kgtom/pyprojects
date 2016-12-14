
'''
定义函数时，需要确定函数名和参数个数；

如果有必要，可以先对参数的数据类型做检查；

函数体内部可以用return随时返回函数结果；

函数执行完毕也没有return语句时，自动return None。

函数可以同时返回多个值，但其实就是一个tuple。
'''
import os
x=3
print x

print range(1,3)
print range(0,3)
print range(-5,-3)

l=[]
for x in range(1,11):
   l.append(x*x)

print l 
print [x*x for x in range(1,11) if x %2==0]

print [d for d in os.listdir('.')]

aa="abc"
print isinstance(aa,str)

# 生成器
g = (x * x for x in range(10))
print g
for n in g:
   print n