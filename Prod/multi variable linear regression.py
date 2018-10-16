import pandas as pd
import numpy as np
from sklearn import linear_model

df = pd.read_csv("auto.csv.csv")

import math
med_km = math.floor(df.km.median())

df.km = df.km.fillna(med_km)

reg = linear_model.LinearRegression()
reg.fit(df[['ps','km']],df.preis)
reg.coef_
reg.intercept_

a = reg.predict([[425,67445]])


print(a) 
