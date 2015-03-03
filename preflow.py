def preflow(a,c,f,st,en,lbd):#a is node set
    backup=[]
    for i in a:
        backup.append((i,c[i].copy(),f[i].copy()))
    n=len(a)
    d={}
    for i in c[st]:
        c[st][i]=c[i][st]=f[i][st]=(c[st][i]*lbd).real
    for i in a:
        d[i]=0
    d[st]=n
    active=[st]
    e={}
    for i in a:
        e[i]=0
    while len(active)>0:
        x=active[0]
        if e[x]<1e-8 and x!=0:
            del active[0]
            continue
        finish=False
        for i in c[x]:
            if f[x][i]<c[x][i] and d[x]>d[i]:
                enow=e[x]
                if x==st:
                    enow=1e10
                ff=min(enow,c[x][i]-f[x][i])
                e[x]-=ff
                e[i]+=ff
                f[x][i]+=ff
                f[i][x]-=ff
                if e[i]>1e-8 and not i in active and i!=st and i!=en:
                    active.append(i)
                if ff==0:
                    del active[0]
                    finish=True
                    break
        if finish:
            continue
        if x!=st:
            mind=1e10
            for i in c[x]:
                if f[x][i]<c[x][i] and d[i]<mind:
                    mind=d[i]
            d[x]=mind+1
        if len(active)>0 and active[0]==st:
            del active[0]
    q=[st]
    used={}
    while len(q)>0:
        x=q[0]
        for i in c[x]:
            if not i in a:
                continue
            if not i in used and f[x][i]<c[x][i]-1e-8:
                d[i]=d[x]+1
                used[i]=1
                q.append(i)
        del q[0]
    q=[en]
    used={}
    while len(q)>0:
        x=q[0]
        for i in a:
            if i in f[x] and not i in used and f[i][x]<c[i][x]-1e-8:
                d[i]=d[x]+1
                used[i]=1
                q.append(i)
        del q[0]
    t1=[i for i in d if d[i]>=n]
    t2=[i for i in d if d[i]<n]
    t3=[i for i in a if not i in d]
    global ans,dm,D
    for i in t3:
        if i in dm:
            for j in D[dm[i]]:
                ans[j]=-1*lbd.imag
    for i in backup:
        x,y,z=i
        c[x]=y
        f[x]=z
    print a,e[en],lbd,d
    return e[en],t1,t2,t3


                
        
    
