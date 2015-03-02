import numpy as np
import xlwt as wt
f=file('res3.txt','r')
a={}
data=f.readlines()
for i in data:
    x,y=i.split()
    if not x in a:
        a[x]=[float(y)]
    else:
        a[x].append(float(y))
wb=wt.Workbook()
sheet=wb.add_sheet("data")
sheet.write(0,0,'num of vertexes')
sheet.write(1,0,'mean')
sheet.write(2,0,'std')
cnt=1
for i in a:
    sheet.write(0,cnt,i)
    sheet.write(1,cnt,np.mean(a[i]))
    sheet.write(2,cnt,np.std(a[i]))
    cnt+=1
wb.save('std.xls')