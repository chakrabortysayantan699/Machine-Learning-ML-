
import numpy as np
import matplotlib.pyplot as plt

cur_x=7 # starting point 
lr_rate=0.2 # learning rate
precision= 0.00001#when i should stop(you can change it )
max_iter=500# maximum iteration(you can change as your wish) 
df=lambda x: 2*x # derivative of fuction
prev_stepsize=1.0# the step size it takes
iters=0 #counter for iterations 
x_up=[]# it will save all the value of x
y_up=[]# it saves cordinate axis

def gradient_decent(cur_x,lr_rate,df,precision=0.00001,max_iter=500,prev_stepsize=1.0,iters=0):
    while (prev_stepsize>precision and iters<max_iter):        
        prev_x=cur_x
        cur_x=cur_x-lr_rate*df(prev_x)
        prev_stepsize=np.abs(cur_x-prev_x)
        iters+=1
        y=cur_x**2
        x_up.append(cur_x)
        y_up.append(y)
        #plt.scatter(cur_x,y)
        plt.plot(cur_x,y,linestyle='--', marker='o')# this plot the points on curve 
        print("Iteration",iters,"value is",cur_x)#it will  print every step in curve
    print("local mninimum occurs at",cur_x)#the local optimum point 


gradient_decent(8,0.1,lambda x :2 *x)

x=np.linspace(-6,6,100)
y=x**2 # my function 
plt.plot(x,y)# this plot fuction
plt.plot(x_up,y_up)# this plot the conncetory line
plt.show()
