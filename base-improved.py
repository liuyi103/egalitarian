import time
f=file('data.txt','r')
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
import os
os.system("code2.exe")
f2=file("divide.txt",'r')
T=int(f2.readline())
match={}
for i in range(T/2):
    x,y=f2.readline().split()
    match[int(x)]=int(y)
    match[int(y)]=int(x)
f2.close()
E={}
M=[]
C={}
used={}
for t in range(n):
    if not t in match:
        C[t]=1
        Q=[t]
        while len(Q)>0:
            i=Q[0]
            del Q[0]
            for j in conn[i]:
                if j in match and not j in used:
                    used[j]=1
                    Q.append(match[j])
                    C[match[j]]=1
for i in range(n):
    if not i in C:
        flag=False
        for j in C:
            if j in conn[i]:
                M.append(i)
                flag=True
                break
        if not flag:
            E[i]=1
#what I will do next is graph construction
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
useM={}
Dm={}
MC={}
for i in range(len(D)):
    for j in D[i]:
        Dm[j]=i
for i in range(n):
    for j in conn[i]:
        if i in Dm and j in M:
            MC[j,Dm[i]]=1
dieM={}
finishD=[]
ans={}
def enumM(x,tm):
    if time.time()-time1>500:
        f3=file('res_base_improved.txt','a')
        f3.write('500+\n')
        exit(0)
    if x==len(M):
        dieD={}
        for i in range(len(D)):
            if i in finishD:
                dieD[i]=1
                continue
            for j in M:
                if (j,i) in MC and not j in tm and not j in dieM:
                    dieD[i]=1
                    break
        td=[]
        for i in range(len(D)):
            if not i in dieD:
                td.append((len(D[i]),D[i],i))
        td=sorted(td,key=lambda td:td[0])
        bf=1e10
        res=[]
        ISI=0.0
        for i in range(len(td)):
            ISI+=td[i][0]
            ff=(ISI-(i+1)+len(tm))/ISI
            if ff<bf:
                bf=ff
                res.append(td[i][2])
            else:
                break
        return bf,res,tm[:]
    tf1,tres1,mm1=enumM(x+1,tm)
    tm.append(M[x])
    tf2,tres2,mm2=enumM(x+1,tm)
    del tm[len(tm)-1]
    if tf1<tf2:
        return tf1,tres1,mm1
    else:
        return tf2,tres2,mm2
for i in E:
    ans[i]=1
for i in M:
    ans[i]=1
while True:
    ff,res,mm=enumM(0,[])
    if len(res)==0:
        break
    for i in mm:
        dieM[i]=1
    for i in res:
        finishD.append(i)
        for j in D[i]:
            ans[j]=ff
f3=file('res_base_improved.txt','a')
f3.write(str(time.time()-time1)+'\n')
# for i in ans:
#     f3.write(str(i)+' '+str(ans[i])+'\n')
# f3.close()
        
