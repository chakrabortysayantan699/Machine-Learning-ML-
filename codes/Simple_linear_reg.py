#import libaries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from jupyterthemes import jtplot as jt

#import dataset
data=pd.read_csv('./simple_regression_data.csv')
#this returns a DataFrame

#Visualizing datasets 
data

#visulaizing the data points ....here we will look how corelated they are 
jt.style()
plt.scatter(data['Volume'],data['Price'],color="orange")
plt.xlabel("Vloume")
plt.ylabel("Price")
plt.title("Volume vs Price")

#Now spliting the dataset for training  and testing 
x_train,x_test,y_train,y_test=train_test_split(data['Volume'],data['Price'],test_size=0.3)
#here we divided the datatset into 70:30 for training and testing

#now predicting comes to play
reg=LinearRegression()
#training is done by fitting traing datasets
reg.fit(pd.DataFrame(x_train),pd.DataFrame(y_train))
#prdicting the value on the test datasets
x_predict=reg.predict(pd.DataFrame(x_test))
y_predict=reg.predict(pd.DataFrame(y_test))

#ploting our predicting value with our testing datasets
plt.scatter(x_test,y_test,color="orange")
plt.plot(x_test,x_predict,color="red")
plt.legend(["predicted hyphothesis","testing datasets"])

plt.show()
