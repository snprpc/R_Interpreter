
import numpy as np
class Rmath:
    ##############
    #函数列表
    ##############
    Function = {
        'sum':'Rsum',
        'prod':'Rprod',
        'max':'Rmax',
        'min':'Rmin',
        'mean':'Rmean',
        'median':'Rmedian',
        'std':'Rstd',
        'var':'Rvar',
        'sort':'Rsort',
        'rev':'Rrev',
        'pmin':'Rpmin',
        'pmax':'Rpmax',
        'match':'Rmatch',
        'union':'Runion',
        'instersect':'Rinstersect',
        'abs':'Rabs',
        'sqrt':'Rsqrt',
        'log':'Rlog',
        'exp':'Rexp',
        'log10':'Rlog10',
        'sin':'Rsin',
        'cos':'Rcos',
        'tan':'Rtan',
        'asin':'Rasin',
        'acos':'Racos',
        'atan':'Ratan',
        'choose':'Rchoose',
        'unique':'Runique',
        'round':'Rround'
    }

    ##############
    #常用函数
    ##############

    ##############
    #R语言向量操作
    ##############

    #R语言sum函数
    def Rsum(self,X):
        result = 0
        for i in X:
            result += i
        return result

    #R语言prod函数
    def Rprod(self,X):
        result = 1
        for i in X:
            result *= i
        return result

    #R语言函数prod(start_num,end_num)
    def Rprod(self,start_num,end_num):
        result = 1
        for i in range(start_num,end_num):
            result *= i
        return result

    #R语言max函数
    def Rmax(self,X):
        result = max(X)
        return result

    #R语言min函数
    def Rmin(self,X):
        result = min(X)
        return result

    #R语言mean函数
    def Rmean(self,X):
        result = float(sum(X) / len(X))
        return result

    #R语言median函数
    def Rmedian(self,X):
       result = np.median(X)
       return result

    #R语言std函数
    def Rstd(self,X):
        result = np.std(X)
        return result

    #R语言var函数
    def Rvar(self,X):
        result = np.var(X)
        return result

    #R语言sort函数
    def Rsort(self,X):
        np.sort(X)

    #R语言rev函数
    def Rrev(self,X):
        sorted(X,reverse=True)

    #R语言pmin函数
    def Rpmin(self,X,Y):
        result = []
        for i in range(len(X)):
            if(X[i] <= Y[i])
                result.append(X[i])
            else
                result.append(Y[i])
        return result

    #R语言pmax函数
    def Rpmax(self,X,Y):
        result = []
        for i in range(len(X)):
            if(X[i] >= Y[i])
                result.append(X[i])
            else
                result.append(Y[i])
        return result

    #R语言match函数
    def Rmatch(self,X,Y):
        result = []
        for i in range(len(X)):
            find = False
            for j in range(len(Y)):
                if X[i] == Y[j]:
                    result.append(j)
                    find = True
                if !find :
                    result.append("NA")
        return result

    #R语言union函数
    def Runion(self,X,Y):
        result = []
        result.append(X)
        result.append(Y)
        return result

    #R语言intersect函数
    def Rinstersect(self,X,Y):
        result = []
        for i in X:
            for j in Y:
                if i == j:
                    result.append(i)
                    break
        return result

    ##############
    #数学函数
    ##############

    #R语言abs函数
    def Rabs(self,X):
        result = np.abs(X)
        return result

    #R语言sqrt函数
    def Rsqrt(self,X):
        result = np.sqrt(X)
        return result

    #R语言log函数
    def Rlog(self,X):
        result = np.log(X)
        return result

    #R语言exp函数
    def Rexp(self,X):
        result = np.exp(X)
        return result

    #R语言log10函数
    def Rlog10(self,X):
        result = np.log10(X)
        return result

    #R语言sin函数
    def Rsin(self,X):
        result = np.sin(X)
        return result

    #R语言cos函数
    def Rcos(self,X):
        result = np.cos(X)
        return result

    #R语言tan函数
    def Rtan(self,X):
        result = np.tan(X)
        return result

    #R语言asin函数
    def Rasin(self,X):
        result = np.asin(X)
        return result

    #R语言acos函数
    def Racos(self,X):
        result = np.acos(X)
        return result

    #R语言atan函数
    def Ratan(self,X):
        result = np.atan(X)
        return result

    #R语言choose函数
    def Rchoose(self,X,Y):
        result = np.choose(X,Y)
        return result

    #R语言unique函数
    def Runique(self,X):
        result = np.unique(X)
        return result

    #R语言round函数
    def Rround(self,X,Y):
        result = round(X,Y)
        return result
