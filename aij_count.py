f1=file('res_base.txt','r')
f2=file('res_base_improved.txt','r')
f3=file('res_fast.txt','r')
data1=[float(i) for i in f1.readlines()]
data2=[float(i) for i in f2.readlines()]
data3=[float(i) for i in f3.readlines()]
data=[data1,data2,data3]
for k in range(3):
    print 'the result of %d'%(k+1)
    print 'num\tgood\tavg\tgood\tavg'
    for i in range(10):
        s=str((i+1)*10)
        g1,g2,cnt1,cnt2=0.,0.,0.,0.
        for j in range(10):
            if j%2==0 and data[k][i*10+j]<240:
                g1+=1
                cnt1+=data[k][i*10+j]
            if j%2==1 and data[k][i*10+j]<240:
                g2+=1
                cnt2+=data[k][i*10+j]
        s+='\t%d\t%.2lf\t%d\t%.2lf'%(g1,g1 and cnt1/g1 or 240,g2,g2 and cnt2/g2 or 240)
        print s
    
                