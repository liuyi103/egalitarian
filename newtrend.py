import numpy as np
import matplotlib.pyplot as pt
f=file('newtrend.txt','r')
base=np.r_[100:1100:100]
up=[]
low=[]
mid=[]
avg=[]
tmp=[]
nodex=[]
nodey=[]
for i in f:
    x,y,z=i.split()
    tmp.append(float(z))
    nodex.append(int(x))
    nodey.append(float(z))
    if y=='4':
        up.append(max(tmp))
        low.append(min(tmp))
        avg.append(np.mean(tmp))
        mid.append(np.median(tmp))
        tmp=[]
#matplotlib.rcParams['axes.unicode_minus'] = False
import pylab
pylab.rcParams['legend.loc'] = 'best'
fig,ax=pt.subplots()
ax.plot(nodex,nodey,'o')
pt.plot(base,up,label='worst instance')
pt.plot(base,low,label='best instance')
pt.plot(base,mid,label='median instance')
pt.plot(base,avg,label='mean value')
pylab.legend()
pt.title('Running time of water-filling algorithm')
pt.xlabel('number of nodes')
pt.ylabel('time:s')
pt.show()    
    