def is_odd(n):
    return n % 2 == 1

print filter(is_odd,[1,2,3,5])   

print sorted([36, 5, 12, 9, 21])

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
print f
print f()
for i in range(1,4):
    print i
#返回函数  闭包1
def count():
     fs=[]
     for i in range(1,4):
         def f():
             return i*i
         fs.append(f)
     return fs
f1,f2,f3=count()
print f1
print f1()
print f2
print f2()
print f3                
print f3()

#返回函数  闭包2
def count():
     fs=[]
     for i in range(1,4):
         def f(j=i):
             return j*j
         fs.append(f)
     return fs
f1,f2,f3=count()
print f1
print f1()
print f2
print f2()
print f3                
print f3()

#匿名函数
print map(lambda x: x * x, [1, 2, 3])

#装饰器
import datetime
def now():
    return datetime.datetime.now()    
f=now
print f()
