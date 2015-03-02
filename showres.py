import matplotlib.pyplot as pt
import numpy as np
f=file('res.txt','r')
a=[]
b=[]
c=[]
for i in range(10):
    x,y=f.readline().split()
    a.append(int(x))
    b.append(float(y))
pt.plot(a,b)
pt.xlabel('number of pairs')
pt.ylabel('average time(s)')
pt.show()
