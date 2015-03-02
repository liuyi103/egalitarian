import os
import convert as ct
for i in range(100,1100,100):
    for j in range(10):
        print i,j
        if j % 2:
            os.system('usgen.py '+str(i))
        else:
            os.system('cngen.py '+str(i))
        ct.transfer()
        os.system('ouralgo2.py')