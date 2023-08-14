# -*- coding: utf-8 -*-
"""GradientDescentFinal.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PLm7RQIU80NnBnz4waJdS_tlGe9tYrnm
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

from google.colab import files
uploaded=files.upload()

def loadData():
  df=pd.read_csv("Dataset.csv",header=None)
  df=df.to_numpy()
  x=df[:,0:100]
  y=df[:,100]
  n=x.shape[0]
  d=x.shape[1]
  return x,y,n,d
#unit testing code
x,y,n,d=loadData()
print(x.shape)
print(y.shape)
print(n)
print(d)

#Question 2 part i
#Analytical solution for wml
def computeWML(x,y):
  w_ml=np.matmul(x.T,x)
  w_ml=np.linalg.inv(w_ml)
  w_ml=np.matmul(w_ml,x.T)
  w_ml=np.matmul(w_ml,y)
  return w_ml

def initialize(d):
  w=np.random.rand(d)
  return w

def computeGradient(w):
  #using the formula derived in the notes
  dw=np.matmul(x.T,x)
  dw=np.matmul(dw,w)
  dw=dw-np.matmul(x.T,y)
  dw=2*dw
  return dw

def prediction(x,w):
  y_pred=np.matmul(x,w)
  return y_pred

def updateW(w,dw,alpha):
  wnew=w-alpha*dw
  return wnew

def gradientDescent(n_iter):
  x,y,n,d=loadData()
  w=initialize(d)
  w_ml=computeWML(x,y)
  diff=pd.DataFrame(columns=['Iteration','Cost'])
  result_idx=0
  for iter_num in range(n_iter):
    err=np.linalg.norm(w-w_ml)
    w_old=w
    dw=computeGradient(w)
    w=updateW(w_old,dw,0.000003)
    if iter_num%10==0:
      diff.loc[result_idx]=[iter_num,err]
      result_idx=result_idx+1
  print("Final W after Gradient Descent")
  print(w)
  return w,diff

#plotting error in various iteration between w and w_ml
w,diff=gradientDescent(1800)
diff[:]

def plot():
  plt.plot(diff['Iteration'],diff['Cost'])
  plt.xlabel("Number of iterations")
  plt.ylabel("L2 norm of ||w-wml||")
plot()

