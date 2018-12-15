import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import getfromdb as db

#Dataframe von getfromdb wird gelesen
df_data = db.df_result


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



normalized_df=(df_data-df_data.mean())/df_data.std()



X = normalized_df.iloc[:,2:13]

ones = np.ones([X.shape[0],1])
X = np.concatenate((ones,X),axis=1)
#.value werden von pandas.core.frame.DataFrame zu numpy.ndarray konvertiert
y = normalized_df.iloc[:,1:2].values 
theta = np.zeros([1,12])


def computeCost(X,y,theta):
    tobesummed = np.power(((X @ theta.T)-y),2)
    return np.sum(tobesummed)/(2 * len(X))

def gradientDescent(X,y,theta,iters,alpha):
    cost = np.zeros(iters)
    for i in range(iters):
        theta = theta - (alpha/len(X)) * np.sum(X * (X @ theta.T - y), axis=0)
        cost[i] = computeCost(X, y, theta)
    
    return theta,cost

#hyper parameter werden gesetzt
alpha = 0.01
iters = 1000

g,cost = gradientDescent(X,y,theta,iters,alpha)
print(g)

finalCost = computeCost(X,y,g)
print(finalCost)

fig, ax = plt.subplots()  
ax.plot(np.arange(iters), cost, 'r')  
ax.set_xlabel('Iterations')  
ax.set_ylabel('Cost')  
ax.set_title('Error vs. Training Epoch')  
