import math
import statsmodels.api as sm
import py_apsrtable as ap
f=file('res2.txt','r')
data=f.readlines()
X=[]
Y=[]
for i in data:
    x,y=i.split()
    X.append(math.log(float(x)))
    Y.append(math.log(float(y)))
# Fit regression model
X=sm.add_constant(X)
results = sm.OLS(Y, X).fit()
# Inspect the results
print sorted(results.params.iteritems())
models=[results]
print results
a=ap.generateTable('table.tex',models)
a.create_table('regression', 'tab:reg')