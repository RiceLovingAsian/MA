import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import getfromdb as db
from sklearn import linear_model

#Daten werden von gerfromdb gelesen
df_data = db.df_result

#Spalten benennen
column = list(df_data.columns)

#leere Einträge werden mit 0 ersetzt
df_data[column].replace(['-'], 0,inplace=True)

#Strings werden zu Fliesskommazahlen konvertiert
def convert_string(val):
    """
    Convert the string number value to a float
     - Remove $
     - Remove commas
     - Convert to float type
    """
    new_val = val.replace('-','0')
    return float(new_val)

for column in df_data.columns:
    if df_data[column].dtypes == 'object' :
        df_data[column] = df_data[column].apply(convert_string)


#mit mean normalization werden die Daten normalisiert
normalized_df=(df_data-df_data.mean())/df_data.std()

#Matzitzen werden gemacht
X = normalized_df.iloc[:,2:13]

ones = np.ones([X.shape[0],1])
X = np.concatenate((ones,X),axis=1)

y = normalized_df.iloc[:,1:2].values 


#Multivariable linear regression Modell
lm = linear_model.LinearRegression()
model = lm.fit(X,y)

Score=lm.score(X,y)
print('Score = ',Score)
coefficients = lm.coef_
print('coefficients = ',coefficients)
intercept = lm.intercept_
print('intercept = ',intercept)
