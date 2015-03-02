import numpy as np
import os
base=np.r_[10:110:10]
for i in base:
    for j in range(5):
        os.system('data_gen.py %d'%i)
        os.system('usinglp2.py')
        f=file('lpout.txt','r')
        print i,j,float(f.readline())

        