import xlrd
import numpy as np
import matplotlib.pyplot as plt
wbk=xlrd.open_workbook('trend.xlsx')
sheet=wbk.sheet_by_index(0)
ma,mi,me,avg=[],[],[],[]
x=range(100,1100,100)
for i in range(2,12):
    tmp=[]
    for j in range(1,11):
        tmp+=[sheet.cell(i,j).value]
    ma+=[max(tmp)]
    mi+=[min(tmp)]
    me+=[np.median(tmp)]
    avg+=[np.mean(tmp)]
plt.plot(x,ma,label='worst instance')
plt.plot(x,mi,label='best instance')
plt.plot(x,me,label='median instance')
plt.plot(x,avg,label='mean value')
plt.legend(loc='upper left')
plt.title('Running time of water-filling algorithm')
plt.xlabel('number of nodes')
plt.ylabel('time: second')
plt.show()
