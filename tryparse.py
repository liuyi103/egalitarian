import py_apsrtable
import statsmodels.api as sm
import pandas as pd

#Generate some data to use
data = sm.datasets.longley.load()
print data
df = pd.DataFrame(data.exog, columns=data.exog_name)
y = data.endog
df['intercept'] = 1.

#Generate the OLS output and store it in olsresult
olsresult = sm.OLS(y, df).fit()

#Add the results to a list. The functions require the results to be in a list.
models = [olsresult]
print models

#Check the order of the variable names
print sorted(olsresult.params.iteritems())

#Define the names to replace the variables
replaceNames = ['Armed', 'Gross National Product', 'GNPDEFL', 'Population', 
'Unemployment', 'Year', 'intercept']

#Assign the generateTable class with the initial values
#Print is an alternate option for the output argument
a = py_apsrtable.generateTable('table.tex', models, center = 'True', parens= 'se', sig_level=0.05, var_names = replaceNames)

#Create the table
a.create_table(caption='OLS Results Table', label='tab:ols', model_name = None, stars=True)

