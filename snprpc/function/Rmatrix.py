import numpy as np

#函数列表
Function = {
    'paste':'Rpaste',
    'format':'Rformat',
    'nchar':'Rchar',
    'length':'Rlength',
    'toupper':'Rtoupper',
    'tolower':'Rtolower',
    'substring':'Rsubstring',
    'strsplit':'Rstrsplit',
    'chartr':'Rchartr',
    'grep':'Rgrep',
}
#常用函数
#R语言创建举矩阵
def matrix(data,nrow,ncol,byrow,dimnames):


# R语言t函数 矩阵的行列转置
def Rt(a):
    result = a.T
    return result
#R语言colSums函数 对矩阵的每一列进行求和
def RcolSums(X):
    result = X.sum(axis=0)
    return result

#R语言colSums函数 对矩阵的每一行进行求和
def RrowSums(X):
    result = X.sum(axis=1)
    return result

#R语言colMeans函数 对矩阵的每一列进行求平均值
def RcolMeans(X):
    tmp = X.sum(axis=0)
    result = tmp / X.shape[1]
    return result


# #R语言rowMeans函数 对矩阵的每一行进行求平均值
# def RrowMeans(X):
#     result = len(X)
#     return result
#
# #R语言det函数 解方程的行列式
# def Rdet(X):
#     result =
#     return result
#
# #R语言crossprod函数 解两个矩阵的内积
# def Rcrossprodr(X):
#     result = str.upper(X)
#     return result
# #R语言outer函数 解两个矩阵的外积
# def Router(X):
#     result = str.lower(X)
#     return result
# #R语言diag函数 对矩阵取对角元素
# def Rdiag(X,Y):
#     result = 0
#     for i in X:
#         result += i
#     return result
#R语言solve函数 对矩阵求逆矩阵
def Rsolve(X):
    result = np.linalg.inv(X)
    return result

#R语言eigen函数 对矩阵求解特征值和特征向量
def Reigen(X):
    eigval,eigvec = np.linalg.eig(X)
    return eigval,eigvec