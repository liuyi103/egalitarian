import matplotlib.pyplot as plt
import numpy as np
import pylab
f1=file('new_our.txt','r')
f2=file('new_bas.txt','r')
f3=file('new_imp.txt','r')
f=[f1,f2,f3]
y=[[],[],[]]
l=[[],[],[]]
r=[[],[],[]]
x1=np.r_[10:110:10]
x2=np.r_[10:60:10]
x3=np.r_[10:90:10]
x=[x1,x2,x3]
le1=np.zeros(10)
tmp=[]
for k in range(3):
    for i in f[k]:
        xx,yy,zz=i.split()
        tmp.append(max(0.01,float(zz)))
        if yy=='4':
            y[k].append(np.mean(tmp))
            l[k].append(np.min(tmp))
            r[k].append(np.max(tmp))
            tmp=[]
print l[1]
print l[0]
print l[2]
pylab.rcParams['legend.loc'] = 'best'
fig,ax=plt.subplots()
label=['water-filling','baseline','improved baseline']
for i in range(3):
    #ax.errorbar(x[i],y[i],yerr=[l[i],r[i]],fmt='-o',label='case %s'%label[i])
    ax.errorbar(x[i],y[i],yerr=[np.array(y[i])-np.array(l[i]),np.array(r[i])-np.array(y[i])],fmt='-o',label=label[i])
ax.set_yscale('log')
pylab.legend()
plt.title('Comparison of  algorithms in log range')
plt.xlabel('number of nodes')
plt.ylabel('time:s')
plt.show()            
        