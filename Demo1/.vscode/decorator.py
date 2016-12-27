
#http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386819879946007bbf6ad052463ab18034f0254bf355000

#不懂

def log(func):
    def wrapper(*args,**kw):
        print 'call %s():'%func._name_
        return func(*args,**kw)
    return wrapper
@log
def now():
    print "22"
print now()    
    