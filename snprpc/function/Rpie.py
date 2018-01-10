import numpy as np
import matplotlib.pyplot as plt
import random

def pie(x, labels = [], radius = 1, main = "Pie Chart", clockwise = 90,col=[]):
    colors = ["blue", "red", "coral", "green", "yellow", "orange"]
    if len(labels) == 0:
        for i in range(len(X)):
            labels.append("case%d" % (i))
    if len(col)==0:
        for i in range(len(X)):
            col.append(colors[i%6])
    plt.pie(x=x,labels = labels,radius = radius,colors=col,startangle= clockwise)
    plt.title(main)
    plt.show()
#labels=['China','Swiss','USA','UK','Laos','Spain']
X=[222,42,455,664,454,334]
# colors = ["blue", "red", "coral", "green", "yellow", "orange"]
pie(X)