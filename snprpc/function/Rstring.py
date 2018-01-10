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
}

#常用函数
#R语言paste函数 连接字符串
def Rpaste(X,Y):
    result = X + Y
    return result

#R语言format函数 格式化数字和字符串 ?
def Rformat(X):
    result = 0
    for i in X:
        result += i
    return result

#R语言nchar函数 计算字符串的字符数
def Rnchar(X):
    result = len(X)
    return result

#R语言length函数 计算字符串长度
def Rlength(X):
    result = len(X)
    return result

#R语言toupper函数 字符串大写转换
def Rtoupper(X):
    result = str.upper(X)
    return result

#R语言tolower函数 字符串小写转换
def Rtolower(X):
    result = str.lower(X)
    print(result)
    return result

#R语言substr函数 字符串提取
def Rsubstr(X,start,stop):
    result = X[start:stop]
    return result

#R语言substring函数 字符串提取
def Rsubstring(X,first):
    result = X[first:]
    return result

#R语言strtrim函数 将字符串修剪到特定的显示宽度 ?中文字符需要设置为2倍
def Rstrtrim(X,width):
    result = result = str.replace(X,)
    return result

#R语言strsplit函数 字符串分割
def Rstrsplit(X,split):
    result = X.split(split)
    return result

#R语言chartr函数 字符串替换
def Rchartr(X,Y):
    result = result = str.replace(X,Y)
    return result

#R语言grep函数 字符串匹配 ?
def Rgrep(X,Y):
    result = result = str.replace(X,Y)
    return result
