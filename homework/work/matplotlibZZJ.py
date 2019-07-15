import matplotlib.pyplot as plt
import numpy as np
x_values=list(range(1,100001))
y1_values=[]
y2_values=[]
def getValues(data):
    y1_values.append(data['int'])
    y2_values.append(data['float'])
    
def plotInit():
    plt.subplot(2,2,1)
    plt.title(u"histogram of int data",fontsize=14)
    plt.hist(y1_values, bins=50, alpha=0.5, histtype='stepfilled',
         color='green', edgecolor='black')
    plt.subplot(2,2,2)
    plt.title(u"histogram of int data",fontsize=14)
    plt.hist(y2_values, bins=50, alpha=0.5, histtype='stepfilled',
         color='blue', edgecolor='black')
    plt.subplot(2,2,3)
    plt.title(u"plot int data",fontsize=14)
    plt.scatter(x_values,y1_values,edgecolor='none',s=1)
    plt.xlabel("each data",fontsize=14)
    plt.ylabel("value",fontsize=14)
    plt.tick_params(axis='both',which='major',labelsize=10)  
    plt.subplot(2,2,4)
    plt.title(u"plot float data",fontsize=14)
    plt.scatter(x_values,y2_values,edgecolor='none',s=1)
    plt.xlabel("each data",fontsize=14)
    plt.ylabel("value",fontsize=14)
    plt.tick_params(axis='both',which='major',labelsize=10)  
    plt.show()
    

def test():
    """
    测试import是否成功
    """
    print("import matplotlibZZJ succeeded")