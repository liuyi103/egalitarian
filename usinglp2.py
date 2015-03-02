import cplex as cp
import time
import pulp as pp
f=file('data.txt','r')
f3=file('resa.txt','w')
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
md={}
nD=[]
p=0
# for i in M:
#     for k in range(len(D)):
#         flag=False
#         for j in D[k]:
#             if j in conn[i]:
#                 md[i,p]=1
#                 flag=True
#         if flag:
#             nD+=[D[k]]
#             p+=1
for i in range(len(D)):
    flag=False
    for j in M:
        if j in conn[i]:
            flag=True
    if flag:
        nD+=[D[i]]
D=nD
for i in M:
    for j in range(len(D)):
        for k in D[j]:
            if i in conn[k]:
                md[i,j]=1
                break
numd=len(D)
nd=[len(i) for i in D]
print D,md
gotten={}
#####################
# prob=cplex.Cplex()
# prob.objective.set_sense(prob.objective.sense.maximize)
# prob.variables.add( lb=[0]*numd, names=['a%d'%i for i in range(numd)])
# prob.variables.add(lb=[0]*len(md),names=['b_%d_%d'%(x,y) for (x,y) in md])
# prob.linear_constraints.add(lin_expr=[cplex.SparsePair(ind=['b_%d_%d'%(x,y) for (x,y) in md if x==i],val=[1.0 for (x,y) in md if x==i]) for i in M], senses='L'*len(M),rhs=[1.]*len(M))
# prob.linear_constraints.add(\
#                             lin_expr=[cplex.SparsePair(ind=['b_%d_%d'%(x,y) for (x,y) in md if y==i]+['a%d'%i],val=[-1.0 for (x,y) in md if y==i]+[nd[i]])for i in range(numd)],\
#                             senses='E'*(numd),rhs=[nd[i] for i in range(numd)])
# tmp=[]
# for i in range(numd):
#     prob.objective.set_linear('a%d'%i,1)
#     prob.linear_constraints.add(lin_expr=[cplex.SparsePair(ind=['a%d'%i,'a%d'%j],val=[-1,1])for j in range(numd) if i-j], senses='G'*(numd-1), rhs=[0]*(numd-1), names=[str(i)+'_'+str(j)for j in range(numd) if i-j])
#     prob.solve()
#     tmp+=[prob.solution.get_objective_value()]
#     prob.linear_constraints.delete([str(i)+'_'+str(j)for j in range(numd) if i-j])
#     prob.objective.set_linear('a%d'%i,0)
# print tmp
###########
xs={}
prob=cp.Cplex()
prob.objective.set_sense(prob.objective.sense.maximize)
prob.variables.add(lb=[0]*len(md), ub=[1]*len(md), names=['b%d_%d'%i for i in md])
prob.variables.add(lb=[0]*numd, ub=[1]*numd, names=['a%d'%i for i in range(numd)])
prob.variables.add(lb=[0],ub=[1],names=['z'])
for i in range(numd):
    prob.linear_constraints.add([[['a%d'%i]+['b%d_%d'%j for j in md if j[1]==i],[len(D[i])]+[-1 for j in md if j[1]==i]]],['E'],[len(D[i])-1])
prob.linear_constraints.add(lin_expr=[[['a%d'%i]+['z'],[1,-1]]for i in range(numd)],senses=['G']*numd,rhs=[0]*numd,names=['z%d'%i for i in range(numd)])
prob.linear_constraints.add([[['b%d_%d'%(i,j)for j in range(numd) if (i,j) in md ],[1 for j in range(numd) if (i,j) in md]] for i in M],['L']*len(M),[1]*len(M))
while len(xs)<numd:
    best,besti=-1,-1
    curr=1
    for curr in range(numd):
        if not curr in xs:
            prob.linear_constraints.add(lin_expr=[[['a%d'%curr,'z'],[1,-1]]],senses='E',rhs=[0],names=['tmp'])
            prob.solve()
            try:
                if prob.solution.get_objective_value()>best:
                    besti=curr
                    best=prob.solution.get_objective_value()
            except:
                pass
            prob.linear_constraints.delete('tmp')
    print besti,best
    xs[besti]=best
    prob.linear_constraints.add([[['a%d'%besti],[1]]],['E'],[best])
    prob.linear_constraints.delete('z%d'%besti)
out=file('lpout.txt','w')
out.write('%f'%(time.time()-time1))




