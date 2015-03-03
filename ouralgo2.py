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
M={}
C={}
used=[]
for t in range(n):
    if not t in match:
        C[t]=1
        Q=[t]
        while len(Q)>0:
            i=Q[0]
            del Q[0]
            for j in conn[i]:
                if j in match and not j in used:
                    used.append(j)
                    Q.append(match[j])
                    C[match[j]]=1
for i in range(n):
    if not i in C:
        flag=False
        for j in C:
            if j in conn[i]:
                M[i]=1
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
Dm={}
for i in range(len(D)):
    for j in D[i]:
        Dm[j]=i
graph={}
gm={}
gm['s']=0
gm['t']=2*n+len(M)+1
N=2*n+2+len(M)
mcnt=0
for i in range(n):
    gm['a'+str(i)]=i+1
    gm['b'+str(i)]=i+n+1
    if i in M:
        gm['c'+str(i)]=2*n+1+mcnt 
        mcnt+=1
for i in range(N):
    graph[i]={}
for i in range(n):
    graph[gm['s']][gm['a'+str(i)]]='special'
    graph[gm['b'+str(i)]][gm['t']]=1
    if not i in C:
        graph[gm['a'+str(i)]][gm['b'+str(i)]]=1
    for j in conn[i]:
        if i in C and j in M :
            graph[gm['a'+str(i)]][gm['c'+str(j)]]=1
    if i in M:
        graph[gm['c'+str(i)]][gm['t']]=1
for i in D:
    for j in i:
        for tk in range(1,len(i)):
            k=i[tk]
            graph[gm['a'+str(j)]][gm['b'+str(k)]]=1
#------------------------------------------------
a=graph
on=n
n=N-1
d=[n+1]
for i in range(1,n+1):
    d.append(0)
e={}
c={}
f={}
for i in range(n+1):
    c[i]={}
    f[i]={}
    e[i]=0
for i in a:
    for j in a[i]:
        tmp=a[i][j]
        if tmp=='special':
            tmp=0
        c[i][j]=tmp
        c[j][i]=tmp
        f[j][i]=tmp
        f[i][j]=0
acc=0.001
basespeed=acc*len(c[0])
baseflow=0
def red():#rearrange d
    global d,c,f
    nd=d[:]
    q=[0]
    used={0:1}
    while len(q)>0:
        x=q[0]
        for i in range(n):
            if i in f[x] and not i in used and f[x][i]<c[x][i]:
                nd[i]=nd[x]+1
                used[i]=1
                q.append(i)
        del q[0]
    q=[n]
    used={}
    while len(q)>0:
        x=q[0]
        for i in range(n):
            if i in f[x] and not i in used and f[i][x]<c[i][x]:
                nd[i]=nd[x]+1
                used[i]=1
                q.append(i)
        del q[0]
    return nd
def addflow():
    global c,f,acc
    for i in c[0]:
        c[0][i]+=acc
        c[i][0]+=acc
        f[i][0]+=acc
ans={}
lnd=d[:]
def preflow():
    global a,n,d,e,c,f,ans,basespeed,baseflow,lnd
    addflow()
    active=[0]
    while len(active)>0:
        x=active[0]
        if e[x]<1e-8 and x!=0:
            del active[0]
            continue
        flag=False;
        finish=False
        for i in c[x]:
            if f[x][i]<c[x][i] and d[x]>d[i]:
                enow=e[x]
                if x==0:
                    enow=1e10
                ff=min(enow,c[x][i]-f[x][i])
                e[x]-=ff
                e[i]+=ff
                f[x][i]+=ff
                f[i][x]-=ff
                flag=True
                if e[i]>1e-8 and not i in active and i>0 and i<n:
                    active.append(i)
                if ff==0:
                    del active[0]
                    finish=True
                    break
        if finish:
            continue
        if x!=0:
            mind=1e10
            for i in c[x]:
                if f[x][i]<c[x][i] and d[i]<mind:
                    mind=d[i]
            d[x]=mind+1
        if len(active)>0 and active[0]==0:
            del active[0]
    if abs(basespeed-(e[n]-baseflow))>1e-10:
        nd=red()
        for i in range(n):
            if lnd[i]<=n and nd[i]>n:
                ans[i]=c[0][1]-acc
        lnd=nd
    basespeed=e[n]-baseflow
    baseflow=e[n]
    return e[n],d
while c[0][1]<1+acc+1e-10 and time.time()-time1<500:
    preflow()
f3.write(str(time.time()-time1)+'\n')
# for i in range(1,on+1):
#     f3.write(str(i-1)+' '+str(ans[i])+'\n')
# f3.close()
