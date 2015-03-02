import matplotlib.pyplot as pt
import os
import numpy as np
s=[10,20,30,40,50,60,70,80,90]
mean1=[]
mean2=[]
std1=[]
std2=[]
if False:
    f1=file('datacmp.txt','w')
    f2=file('log.txt','w')
    for i in s:
        tt1=0
        tt2=0
        resa=[]
        resb=[]
        for j in range(10):
            os.system("data_gen.py %d"%i)
#             os.system("ouralgo2.py")
#             f=file('resa.txt','r')
            os.system('usinglp2.py')
            f=file('lpout.txt','r')
            tmp=float(f.readline())
            resa.append(tmp)
            print i,j,tmp
            f2.write("%d %d %f\n"%(i,j,tmp))
        mean1.append(np.mean(resa))
        std1.append(np.std(resa))
ff=file('tmp.txt','r')
tmp=[]
for i in ff:
    x,y,z=i.split()
    tmp.append(float(z))
    if y=='9':
        print tmp
        mean2.append(np.mean(tmp))
        std2.append(np.std(tmp))
        tmp=[]
ff=file('log.txt','r')
tmp=[]
for i in ff:
    x,y,z=i.split()
    tmp.append(float(z))
    if y=='9':
        print tmp
        mean1.append(np.mean(tmp))
        std1.append(np.std(tmp))
        tmp=[]
print mean2,std2
pt.xlabel('number of nodes')
pt.ylabel('time: s')
pt.title('Running time comparison between two algorithms')
pt.plot(s,mean1)
pt.plot(s,mean2)
pt.show()
pt.title('standard error of running time comparison between two algorithms')
pt.xlabel('number of nodes')
pt.ylabel('time: s')
pt.plot(s,std1)
pt.plot(s,std2)
pt.show()
pt.xlabel('number of nodes')
pt.ylabel('lg(time)')
pt.title('Running time comparison between two algorithms')
pt.plot(s,np.log10(mean1))
pt.plot(s,np.log10(mean2))
pt.show()
pt.title('standard error of running time comparison between two algorithms')
pt.xlabel('number of nodes')
pt.ylabel('lg(time)')
pt.plot(s,np.log10(std1))
pt.plot(s,np.log10(std2))
pt.show()
