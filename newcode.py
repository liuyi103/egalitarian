# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 15:48:50 2015

@author: liuyi103
"""

import time
f=file('data.txt','r')
f3=file('res_fast.txt','a')
time1=time.time()
n,m=f.readline().split()
n=int(n)
m=int(m)
a=[]
g={}
conn=[]
for i in range(n):
    conn.append([])
for i in range(m):
    x,y=f.readline().split()
    a.append((int(x),int(y)))
    conn[int(x)].append(int(y))
    conn[int(y)].append(int(x))
    g[x,y]=1
f.close()
#------------
import os
os.system("./code2run")
f2=file("divide.txt",'r')
T=int(f2.readline())
match={}
for i in range(T/2):
    x,y=f2.readline().split()
    match[int(x)]=int(y)
    match[int(y)]=int(x)
f2.close()
#-----------
E={}
M={}
C={}
used=[]
def divdfs(st,hist):
    global M,C
    if st in hist or st in C:
        return
    if st in M:
        del M[st]
    C[st]=1
    for i in conn[st]:
        if i not in match:
            continue
        if match[i]==st:
            continue
        if match[i] in C:
            continue
        if i not in C:
            M[i]=1
        divdfs(match[i],hist+[st,i])
    pass
for i in range(n):
    if i not in match:
        divdfs(i,[])
for i in range(n):
    if i not in C.keys()+M.keys():
        E[i]=1
D=[]
dd=0
dived=[]
for i in C:
    if i in dived:
        continue;
    tset=[i]
    bfs={i:1}
    dived.append(i)
    while len(bfs)>0:
        tbfs={}
        for i in bfs:
            for j in C :
                if not j in dived and j in conn[i]:
                    tbfs[j]=1
                    tset.append(j)
                    dived.append(j)
        bfs=tbfs
    D.append(tset)
Dm={}
for i in range(len(D)):
    for j in D[i]:
        Dm[j]=i
print D,Dm,E,M,C
import networkx as nx
#---------
g=nx.DiGraph()
g.add_edges_from([('st','a%d'%i) for i in range()])

