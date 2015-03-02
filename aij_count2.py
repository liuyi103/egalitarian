f=file('res_fast.txt','r')
data=[float(i) for i in f.readlines()]
print 'num\t1\t2\t3\t4\t5\t1\t2\t3\t4\t5'
for i in range(10):
    s=str((i+1)*100)
    out=[]
    for j in range(10):
        if j%2==0:
            out+=[data[i*10+j]]
    for j in range(10):
        if j%2==1:
            out+=[data[i*10+j]]
#     print 's+=\''+'\\t%.1lf'*10+'\'%out'
#     exec 's+=\''+'\%.1lf'*10+'\'\%out'
    s+='\t%.1lf\t%.1lf\t%.1lf\t%.1lf\t%.1lf\t%.1lf\t%.1lf\t%.1lf\t%.1lf\t%.1lf'%(out[0],out[1],out[2],out[3],out[4],out[5],out[6],out[7],out[8],out[9])
    print s