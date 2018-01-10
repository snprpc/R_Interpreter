import matplotlib.pyplot as plt
import numpy as np

#函数列表
Function = {
    'barplot':'barplot',
    'plot':'line',
    'pie':'pie',
    'hist':'hist',

}
#####################################################
#条形统计图
#参数：高度，X轴标志，图形名称，颜色，x轴名称
#
#####################################################
def barplot(H, names=[],  main = "bar char", col = "black", xlab = "X-axis", ylab = "Y-axis"):
    width = 0.8
    # make a square figure
    fig = plt.figure()
    #对X轴标签进行处理
    if len(names) == 0:
        for i in range(len(H)):
          names.append(" ")
    X = []
    for i in range(len(names)):
        X.append(i)
    print (X)
    for i in X:
        print(i)
    plt.xticks(X,names) #显示X轴标签
    plt.bar(X,H,width,color=col)#画条形统计图
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(main)
    plt.show()

def barplot(H, names=[],  main = "bar char", col = "black", xlab = "X-axis", ylab = "Y-axis"):
    width = 0.8
    # make a square figure
    fig = plt.figure()
    #对X轴标签进行处理
    if len(names) == 0:
        for i in range(len(H)):
          names.append(" ")
    X = []
    for i in range(len(names)):
        X.append(i)
    print (X)
    for i in X:
        print(i)
    plt.xticks(X,names) #显示X轴标签
    plt.bar(X,H,width,color=col)#画条形统计图
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(main)
    plt.show()

####################################################################
#折线图
#参数：数据、点的类型、颜色、X轴标识、y轴标识、标题
#
####################################################################
def line(V,type = "o",col = "black",xlab = "X",ylab = "Y",main = "plot"):
    plt.figure()
    X = []
    for i in range(len(V)):
        X.append(i + 1)
    plt.plot(X,V,color=col,marker = type,linewidth = 1)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(main)
    plt.show()

##################################################################
#饼状图
#参数：数据、每一块的名称、半径、标题、画图方向、颜色
#
#################################################################

def pie(x,col,labels = [], radius = 1, main = "Pie Chart", clockwise = 90):
    colors = ["blue", "red", "coral", "green", "yellow", "orange"]
    if len(labels) == 0:
        for i in range(len(X)):
            labels.append("case%d" % (i))
    plt.pie(x=x,labels = labels,radius = radius,colors=col,startangle= clockwise)
    plt.title(main)
    plt.show()

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

########################################################
# #labels=['China','Swiss','USA','UK','Laos','Spain']
# X=[222,42,455,664,454,334]
# # colors = ["blue", "red", "coral", "green", "yellow", "orange"]
# pie(X)


##############################################################################
#散点图
#参数：X轴数据、Y轴数据、X轴最大值，Y轴最大值，标题、X轴标签、Y轴标签、是否画X\Y轴
#
#############################################################################
def dot(X,Y,xlim,ylim,main = "Scatterplot",xlab = "X",ylab = "Y",axes = "True"):
    plt.title(main)
    plt.xlim(xmax=xlim,xmin=0)
    plt.ylim(ymax=ylim,ymin=0)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.plot(X,Y,'ro')
    plt.legend(axes,loc=2)
    plt.show()

######################################################
# v=[0,9,13,21,8,36,22,12,41,31,33,19]
# y=[0,9,13,21,8,36,22,12,41,31,33,19]
# dot(v,y,40,40)

#################################################################################
#直方图
#参数：数据、X轴最大值，Y轴最大值，标题、X轴标签、Y轴标签、条数、颜色、边框
#
################################################################################
def hist(V,xlim,ylim,main = "histogram",xlab = "Weight",ylab = "Frequency",breaks = 10,col = "blue",border = "blue"):
    plt.title(main)
    plt.xlim(xmax=xlim, xmin=0)
    plt.ylim(ymax=ylim, ymin=0)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.hist(V,facecolor=col,bins = breaks, edgecolor =  border)
    plt.show()


###################################################################################
# v=[0,9,13,21,8,36,22,12,41,31,33,19]
# hist(v,main = "histogram", xlab = "Weight",ylab = "Frequency",border = "red", xlim = 40, ylim = 5,
#    breaks = 5)