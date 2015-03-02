def transfer():
    f=file('output.txt','r')
    a=[]
    s=f.readline()
    exec 'a='+s
    n=len(a)
    edge=[(i,j) for i in range(n) for j in range(i+1,n) if a[i][j]>0.1 and a[j][i]>0.1]
    f.close()
    f=file('data.txt','w')
    f.write('%d %d\n'%(n,len(edge)))
    for i in edge:
        f.write('%d %d\n'%(i[0],i[1]))