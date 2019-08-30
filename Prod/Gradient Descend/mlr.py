import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import getfromdb as db

#Reading dataframe from getfromdb
df_data = db.df_result


column = list(df_data.columns)

#Replacing - entries with 0
df_data[column].replace(['-'], 0,inplace=True)

#converting string column into float 
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


#setting the matrixes
X = normalized_df.iloc[:,2:13]
#adding intercept
ones = np.ones([X.shape[0],1])
X = np.concatenate((ones,X),axis=1)

y = normalized_df.iloc[:,1:2].values #.values converts it from pandas.core.frame.DataFrame to numpy.ndarray
theta = np.zeros([1,12])

#compute cost
def computeCost(X,y,theta):
    tobesummed = np.power(((X @ theta.T)-y),2)
    return np.sum(tobesummed)/(2 * len(X))

def gradientDescent(X,y,theta,iters,alpha):
    cost = np.zeros(iters)
    for i in range(iters):
        theta = theta - (alpha/len(X)) * np.sum(X * (X @ theta.T - y), axis=0)
        cost[i] = computeCost(X, y, theta)
    
    return theta,cost

#set hyper parameters
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
