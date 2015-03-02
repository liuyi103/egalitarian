import time
time1=time.time()
def dfs(a,i,used,cnt):
    global bestcnt
    global pcnt
    global times
    if i==len(a):
        if cnt>bestcnt:
            bestcnt=cnt
            pcnt={}
            for j in used:
                pcnt[j]=1
            times=1
        elif cnt==bestcnt:
            for j in used:
                if j in pcnt:
                    pcnt[j]+=1
                else:
                    pcnt[j]=1
            times+=1
        return cnt
    tmp=0
    if not(a[i][0] in used or a[i][1] in used):
        used[a[i][0]]=1
        used[a[i][1]]=1
        tmp=dfs(a,i+1,used,cnt+1)
        del used[a[i][0]]
        del used[a[i][1]]
    return max(tmp,dfs(a,i+1,used,cnt))
def CC(J):
    ans={}
    for i in J:
        for j in match[i]:
            if not j in usedO:
                ans[j]=1
    return ans
def func(J):
    global O
    global a
    t1=0.0
    for i in J:
        t1+=len(D[i])
    return (t1-(len(J)-len(CC(J))))/t1
usedD={}
minf=100
minJ={}
def maindfs(x,J):
    if time.time()-time1>240:
        out=file('res_base.txt','a')
        out.write('241\n')
        exit(0)
    global D
    global minJ
    global minf
    global usedD
    if x==len(D):
        if len(J)==0:
            return
        tmpf=func(J)
        if tmpf<minf:
            minf=tmpf
            minJ={}
            for i in J:
                minJ[i]=1
        return
    if not x in usedD:
        J[x]=1
        maindfs(x+1,J)
        del J[x]
    maindfs(x+1,J)
bestcnt=0
pcnt={}
times=0
f=file('data.txt','r')
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
##best=dfs(a,0,{},0)
U=[]
O=[]
P=[]
tmpl={}
usedO={}
##for i in range(n):
##    if i not in pcnt or pcnt[i]<times:
##        U.append(i)
##for i in range(n):
##    if not i in U:
##        flag=True
##        for j in U:
##            if (i,j) in a or (j,i) in a:
##                O.append(i)
##                flag=False
##                break
##        if flag:
##            P.append(i)
#until now, sets divided
D=[]
dd=0
dived=[]
##for i in U:
##    if i in dived:
##        continue;
##    tset=[i]
##    bfs={i:1}
##    dived.append(i)
##    while len(bfs)>0:
##        tbfs={}
##        for i in bfs:
##            for j in U :
##                if not j in dived and ((i,j) in a or (j,i) in a):
##                    tbfs[j]=1
##                    tset.append(j)
##                    dived.append(j)
##        bfs=tbfs
##    D.append(tset)
#the following is added#
############
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
O=M
P=E.keys()
U=C.keys()
##################
match={}
for i in range(len(D)):
    tmp=[]
    for j in D[i]:
        for k in O:
            if (j,k) in a or (k,j) in a:
                tmp.append(k)
    match[i]=tmp;
#D gotten
res={}
for i in O:
    res[i]=1
for i in P:
    res[i]=1
while len(usedD)<len(D):
    minf=100
    minJ={}
    maindfs(0,{})
    for i in minJ:
        usedD[i]=1
        for j in D[i]:
            res[j]=minf
        for j in match[i]:
            usedO[j]=1
out=file('res_base.txt','a')
out.write(str(time.time()-time1)+'\n')

