d={'tom':11,'kg':4}
print d['tom']
print 'tom' in d
print d.get('tom2')
print d.pop('tom')

def upper(str):
    return str[0:1].upper() + str[1:].lower()

L = ['adam', 'LISA', 'barT']
for x in map(upper,L):
    print x,

#def str(str):
list=[1,2]
for i in map(str,list):
    print i
def add(x,y):
    return x+y 

print reduce(add,[1,3])    
#def str2int(s):

def  fn(x,y):
     return x+y

#print reduce(str2int,["1"])   
print reduce(fn,["1","4"])     