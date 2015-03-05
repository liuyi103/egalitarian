import time
f=file('data.txt','r')
f3=file('resa.txt','w')
time1=time.time()
n,m=f.readline().split()
n=int(n)
m=int(m)
g={}
conn=[]
tmpcon=[]
for i in range(n):
    conn.append([])
for i in range(m):
    x,y=f.readline().split()
    conn[int(x)].append(int(y))
    conn[int(y)].append(int(x))
    tmpcon.append((int(x),int(y)))
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
print E,M,C
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
print D
Dm={}
for i in range(len(D)):
    for j in D[i]:
        Dm[j]=i
st=0
en=1
a=[0,1]
p=2
ans={}
c=[{},{}]
f=[{},{}]
for i in E:
    ans[i]=1
for i in M:
    ans[i]=1
todel1=[]
for i in C:
    if len(conn[i])==0:
        ans[i]=0
        todel1.append(D[Dm[i]])
for i in todel1:
    D.remove(i)
mm={}
for i in M:
    a.append(p)
    c.append({})
    f.append({})
    c[p][en]=c[en][p]=f[en][p]=1
    f[p][en]=0
    mm[i]=p
    p+=1
dm={}
for x in range(len(D)):
    i=D[x]
    dm[p]=i
    a.append(p)
    c.append({})
    f.append({})
    c[st][p]=c[p][st]=f[p][st]=len(i)*1j
    f[st][p]=0
    if len(i)>1:
        c[en][p]=c[p][en]=f[en][p]=len(i)-1
        f[p][en]=0
    for j in i:
        for k in M:
            if k in conn[j]:
                c[p][mm[k]]=c[mm[k]][p]=f[mm[k]][p]=1
                f[p][mm[k]]=0
    p+=1
def convert(x):
    x=str(x)
    if x[0]!='k':
        return 0,int(x)
    try:
        return int(x[1:]),0
    except:
        x,y=x[1:].split()
        return int(x),int(y)
def add(x,y):
    x1,x2=convert(x)
    y1,y2=convert(y)
    if x1+y1==0:
        return x2+y2
    if x2+y2==0:
        return 'k'+str(x1+y1)
    return 'k'+str(x1+y1)+' '+str(x2+y2)
def merge(a,b):
    global p,c,f
    c.append({})
    f.append({})
    for i in b:
        for j in c[i]:
            if j in a and not j in b:
                if j in c[p]:
                    c[p][j]=c[j][p]=c[j][p]+c[i][j]
                    f[p][j]=f[p][j]+f[i][j]
                    f[j][p]=f[j][p]+f[j][i]
                else:
                    c[j][p]=c[p][j]=c[i][j]
                    f[j][p]=f[j][i]
                    f[p][j]=f[i][j]
    for i in b:
        a.remove(i)
    a.append(p)
    p+=1
def speed(st,sett):
    ans=0
    for i in sett:
        if i in c[st]:
            ans+=c[st][i].imag
    return ans
def getline(flow,lbd,speed):#y=ax+b
    b=flow-speed*lbd
    a=speed
    return a,b
def jiaodian(a1,b1,a2,b2):#return x,y
    x=(b1-b2)/(a2-a1)
    y=a1*x+b1
    return x,y
import preflow
rs={0.0:{},1.0:{}}#result set
rs[0]['flow'],rs[0]['t1'],rs[0]['t2'],rs[0]['t3']=preflow.preflow(a,c,f,st,en,1-0j)
rs[1]['flow'],rs[1]['t1'],rs[1]['t2'],rs[1]['t3']=preflow.preflow(a,c,f,st,en,1-1j)
rs[0]['speed']=speed(st,rs[0]['t2']+rs[0]['t3'])#t2+t3 speed for right,t2->speed left,
rs[1]['speed']=speed(st,rs[1]['t2'])
merge(a,rs[0]['t1']+rs[0]['t3'])
if not st in a:
    st=a[-1]
merge(a,rs[1]['t2']+rs[1]['t3'])
if not en in a:
    en=a[-1]
def dfs(ll,rl,a,st,en):#left-lambda,right-lambda
    global c,f
    if rs[ll]['speed']==rs[rl]['speed']:
        return 
    a1,b1=getline(rs[ll]['flow'],ll,rs[ll]['speed'])
    a2,b2=getline(rs[rl]['flow'],rl,rs[rl]['speed'])
    x,y=jiaodian(a1,b1,a2,b2)
    rs[x]={}
    if len(a)<3:
        return
    rs[x]['flow'],rs[x]['t1'],rs[x]['t2'],rs[x]['t3']=preflow.preflow(a,c,f,st,en,1-x*1j)
    rs[x]['speed']=speed(st,rs[x]['t2'])
    a1=a[:]
    merge(a1,rs[x]['t2']+rs[x]['t3'])
    tenn=en
    if not en in a:
        tenn=a1[-1]
    dfs(ll,x,a1,st,tenn)
    rs[x]['speed']=speed(st,rs[x]['t2']+rs[x]['t3'])
    a1=a[:]
    merge(a1,rs[x]['t1']+rs[x]['t3'])
    tst=st
    if not st in a:
        tst=a1[-1]
    dfs(ll,x,a1,tst,tenn)
dfs(0,1,a,st,en)
print ans
    
    