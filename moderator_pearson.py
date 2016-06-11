# Modulator: Pearson (Q->Q)  
# week4 assignment for Data Analysis Tools

# moderating variable: income per person
# explanator variable: alcohol consumption
# response variable: life expectancy

"""
Created on Sat Jun 11 10:45:24 2016

@author: Taehee Jeong
"""


# import libraries
import pandas as pd
import scipy.stats
import seaborn
import matplotlib.pyplot as plt

import numpy as np
import statsmodels.formula.api as smf
import statsmodels.stats.multicomp as multi 




#%% Load data
path='C:/Bigdata/Data Analysis and Interpretation/Dataset/GapMinder/'
data = pd.read_csv(path+'gapminder.csv', low_memory=False)

print data.columns

#setting variables you will be working with to numeric
data['incomeperperson'] = pd.to_numeric(data['incomeperperson'], errors='coerce')
data['alcconsumption'] = pd.to_numeric(data['alcconsumption'], errors='coerce')
data['lifeexpectancy'] = pd.to_numeric(data['lifeexpectancy'], errors='coerce')

#%% Clean data

# subset of data
features=['alcconsumption','incomeperperson','lifeexpectancy']
sub1=data[features]

# remove row with NA
sub1_clean=sub1.dropna()

#%% modulator variable
sub1_clean.incomeperperson.describe()
sub1_clean.incomeperperson.hist()

def incomegrp (row):
   if row['incomeperperson'] <= 640:
      return 1
   elif row['incomeperperson'] <= 7634 :
      return 2
   elif row['incomeperperson'] > 7634:
      return 3
   
sub1_clean['incomegrp'] = sub1_clean.apply (lambda row: incomegrp (row),axis=1)

chk1 = sub1_clean['incomegrp'].value_counts(sort=False, dropna=False)
print(chk1)

sub1_1=sub1_clean[(sub1_clean['incomegrp']== 1)]
sub1_2=sub1_clean[(sub1_clean['incomegrp']== 2)]
sub1_3=sub1_clean[(sub1_clean['incomegrp']== 3)]

#%% Pearson test: Q->Q
print ('association between alcconsumption and lifeexpectancy for LOW income countries')
print (scipy.stats.pearsonr(sub1_1['alcconsumption'], sub1_1['lifeexpectancy']))
print ('       ')
print ('association between alcconsumption and lifeexpectancy for MIDDLE income countries')
print (scipy.stats.pearsonr(sub1_2['alcconsumption'], sub1_2['lifeexpectancy']))
print ('       ')
print ('association between alcconsumption and lifeexpectancy for HIGH income countries')
print (scipy.stats.pearsonr(sub1_3['alcconsumption'], sub1_3['lifeexpectancy']))

#%%
scat1 = seaborn.regplot(x="alcconsumption", y="lifeexpectancy", data=sub1_1)
plt.xlabel('alcconsumption')
plt.ylabel('lifeexpectancy')
plt.title('Scatterplot for the Association Between alcconsumption and lifeexpectancy for LOW income countries')
print (scat1)
#%%
scat2 = seaborn.regplot(x="alcconsumption", y="lifeexpectancy", data=sub1_2)
plt.xlabel('alcconsumption')
plt.ylabel('lifeexpectancy')
plt.title('Scatterplot for the Association Between alcconsumption and lifeexpectancy for MIDDLE income countries')
print (scat2)
#%%
scat3 = seaborn.regplot(x="alcconsumption", y="lifeexpectancy", data=sub1_3)
plt.xlabel('alcconsumption')
plt.ylabel('lifeexpectancy')
plt.title('Scatterplot for the Association Between alcconsumption and lifeexpectancy for HIGH income countries')
print (scat3)


