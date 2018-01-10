
import numpy as np
import matplotlib.pyplot as plt
def plot(V,type = "o",col = "black",xlab = "X",ylab = "Y",main = "plot"):
    plt.figure()
    X = []
    for i in range(len(V)):
        X.append(i + 1)
    plt.plot(X,V,color=col,marker = type,linewidth = 1)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(main)
    plt.show()
V = [3,4,6,1,2,8,9,12,2,5]
plot(V,"p","blue","X","Y","tilte")
