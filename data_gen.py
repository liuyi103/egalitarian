import sys
try:
    n=int(sys.argv[1])
except:
    n=40
a=0.3373
b=0.1428
ab=0.0385
o=0.4814
hpr_high=0.0981
hpr_low=0.7019
p_high=0.1
p_low=0.95
#patient-donor
info={}
bloodmatch={}
for i in ['a','b','c','o']:
    bloodmatch[(i,'o')]=1
    bloodmatch[('c',i)]=1
    bloodmatch[(i,i)]=1
def blood():
    global a,b,ab,o
    import random
    x=random.random()
    if x<a:
        return 'a'
    if x<a+b:
        return 'b'
    if x <a+b+o:
        return 'o'
    return 'c'
def hpr():
    global hpr_high,hpr_low,p_high,p_low
    import random
    x=random.random()
    if x <hpr_high:
        return p_high
    if x <hpr_low+hpr_high:
        return p_low
    return (p_high+p_low)/2
def match(x,y):
    if not (x['pb'],y['db']) in bloodmatch:
        return False
    p=x['phpr']
    import random
    if p>random.random():
        return True
    return False
for i in range(n):
    info[i]={}
    info[i]["pb"]=blood()
    info[i]['db']=blood()
    info[i]['phpr']=hpr()
    info[i]['dhpr']=hpr()
    if match(info[i],info[i]):
        i-=1
map={}
for i in range(n):
    for j in range(i+1,n):
        if match(info[i],info[j]) and match(info[j],info[i]):
            map[i,j]=1
f=file('data.txt','w')
f.write(str(n)+' '+str(len(map))+'\n')
for i in map:
    x,y=i
    f.write(str(x)+' '+str(y)+'\n')
f.close()
