import os
import csv

Function{
    'getwd':'Rgetwd',
    'setwd':'Rsetwd',
    'read.scv':'Rreadscv',
    'c':'Rc'
}


#R语言getwd函数
def Rgetwd():
    result = os.getcwd()
    return result

#R语言setwd函数
def Rsetwd(X):
    os.chdir(X)

#R语言read.scv函数
def Rreadscv(X):
    result = csv.reader(open(X,encoding='utf-8'))
    return result

#R语言c函数
def Rc(args=[]):
    result = []
    for i in args:
        result.append(i)
    return result