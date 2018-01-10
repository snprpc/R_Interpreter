# -*- coding:utf-8 -*-
__author__ = '1'

from snprpc.LeMorphology.LeScanDict import *
import string
import operator

class MorAnalysis(object):
    # 下标
    _p = 0
    # 存放词法分析出的单词
    _value = ''
    # 种类码
    _syn = ''
    # 字符串状态
    _stringState = 0
    # 数据状态
    _dataState = 0
    # 类型
    _key = ''
    # 存放词法分析的结果
    _tokens = []
    # 存放用来检查结果的token
    _tokenCheck = []
    # 当前下标指示的字符
    _ch = ''

    # 删除多余空格
    def delSpace(self,mystr):
        while self._ch == ' ':
            self._ch = mystr[self._p]
            self._p += 1

    # 检查是否包含非法字符
    def isIllegalChar(self):
        for illegalChar in illegalChars:
            if illegalChar in self._value:
                self._syn = '@-6' #错误代码，标识符中包含非法字符
                break
            else:
                self._key = 'VARIABLE'
                self._syn = 1 # 变量名、函数名

    # 检查是否为关键字
    def isKeyword(self):
        for keyword in keywords:
            if operator.eq(keyword,self._value):
                self._key = 'RESERVED'
                self._syn = LeScanDict[self._value.upper()] #关键字
                break

    def analysisCode(self,mystr):
        self._key = ''
        self._syn = ''
        self._value = ''
        self._ch = mystr[self._p]
        self._p += 1

        self.delSpace(mystr)

        if self._ch in string.ascii_letters:
            # 读出完整的单词、变量名、关键字等
            while self._ch in string.ascii_letters or self._ch in string.digits or self._ch == '_' or self._ch in illegalChars:
                self._value += self._ch
                self._ch = mystr[self._p]
                self._p += 1
            self._p -= 1
            # 检查是否包含非法字符
            self.isIllegalChar()
            # 检查是否为关键字
            self.isKeyword()

        elif self._ch == '.':
            self._value = '.'
            self._key = 'RESERVED'
            self._syn = 42 # '.'

        elif self._ch == '\"':    #字符串
            # while self._ch in string.ascii_letters or self._ch in '\"% ' or self._ch in '.,\'{};':
            while True:
                self._value += self._ch
                if self._stringState == 0:
                    if self._ch == '\"':
                        self._stringState = 1
                elif self._stringState == 1:
                    if self._ch == '\"':
                        self._stringState = 2
                        break

                self._ch = mystr[self._p]
                self._p += 1

            if self._stringState == 1:
                self._syn = '@-2'  #错误代码，字符串不封闭
                self._stringState = 0
            elif self._stringState == 2:
                self._value = self._value.replace('\"','')
                self._key = 'STRING'
                self._syn = 0      # 'STRING' : 0
                self._stringState = 0

            # self._p -= 1

        elif self._ch == "\'":#字符串
            # while self._ch in string.ascii_letters or self._ch in "\'%" or self._ch in '.,\"{}()':
            while True:
                self._value += self._ch
                if self._stringState == 0:
                    if self._ch == "\'":
                        self._stringState = 1
                elif self._stringState == 1:
                    if self._ch == "\'":
                        self._stringState = 2
                        break

                self._ch = mystr[self._p]
                self._p += 1

            if self._stringState == 1:
                self._syn = '@-2'  #错误代码，字符串不封闭
                self._stringState = 0
            elif self._stringState == 2:
                self._value = self._value.replace("\'","")
                self._key = 'STRING'
                self._syn = 0      # 'STRING' : 0
                self._stringState = 0

            # self._p -= 1

        elif self._ch in string.digits:
            while self._ch in string.digits or self._ch == '.' or self._ch in string.ascii_letters:
                self._value += self._ch
                if self._dataState == 0:
                    if self._ch == '0':
                        self._dataState = 1
                    else:
                        self._dataState = 2

                elif self._dataState == 1:
                    if self._ch == '.':
                        self._dataState = 3
                    else:
                        self._dataState = 5

                elif self._dataState == 2:
                    if self._ch == '.':
                        self._dataState = 3

                self._ch = mystr[self._p]
                self._p += 1

            for char in string.ascii_letters:
                if char in self._value:
                    self._syn = '@-7' #错误代码，数字和字母混合，如12AB56等
                    self._dataState = 0

            if self._syn != '@-7':
                if self._dataState == 5:
                    self._syn = '@-3' #错误代码，数字以0开头
                    self._dataState = 0
                else:
                    self._dataState = 0
                    if '.' not in self._value:
                        self._key = 'INTEGER'
                        self._syn = 2               #整数
                    else:
                        if self._value.count('.') == 1:
                            self._key = 'DOUBLE'
                            self._syn = 34           # 浮点数
                        else:
                            self._syn = '@-5' #错误代码，浮点数中包含多个点，如1.2.3
            self._p -= 1

        elif self._ch == '\'':
            self._value =self._ch
            self._key = 'RESERVED'
            self._syn = 3 # '\''

        elif self._ch == '\"':
            self._value = self._ch
            self._key = 'RESERVED'
            self._syn = 4     # '\"'

        elif self._ch == ',':
            self._value = self._ch
            self._key = 'RESERVED'
            self._syn = 5     # ','

        elif self._ch == '(':
            self._value = self._ch
            self._key = 'RESERVED'
            self._syn = 6     # '('

        elif self._ch == ')':
            self._value = self._ch
            self._key = 'RESERVED'
            self._syn = 7     # ')'

        elif self._ch == '{':
            self._value = self._ch
            self._key = 'RESERVED'
            self._syn = 8
            self._ch = mystr[self._p]
            if self._ch == ';':
                self._p += 1


        elif self._ch == '}':
            self._value = self._ch
            self._key = 'RESERVED'
            self._syn = 9     # '}'

        elif self._ch == ';':
            self._value = ';'
            self._key = 'RESERVED'
            self._syn = 10
            if self._p + 1 != mystr.__len__():
                self._ch = mystr[self._p + 1]

                # 去除多余空行
                if self._ch == '\n':
                    self._p += 1
                    self._ch = mystr[self._p]
                    while self._ch == '\n':
                        self._p += 1
                        self._ch = mystr[self._p]

                # 去除‘}’前面的分号
                if self._ch == '}':
                    self._value = self._ch
                    self._key = 'RESERVED'
                    self._syn = 9
                    self._p += 2






        elif self._ch == '+':
            self._value = self._ch
            self._key = 'RESERVED'
            self._syn = 11     # '+'

        elif self._ch == '-':
            self._value = self._ch
            self._ch = mystr[self._p]

            if self._ch == '>':
                self._value += self._ch
                self._p += 1
                self._key = 'RESERVED'
                self._syn = 30     # '->'
                self._ch = mystr[self._p]
                if self._ch == '>':
                    self._value += self._ch
                    self._p += 1
                    self._key = 'RESERVED'
                    self._syn = 30     # '->>'

            else:
                self._key = 'RESERVED'
                self._syn = 12       # '-'

        elif self._ch == '*':
            self._value = self._ch
            self._key = 'RESERVED'
            self._syn = 13     # '*'

        elif self._ch == '/':
            self._value = self._ch
            self._key = 'RESERVED'
            self._syn = 14     # '/'

        elif self._ch == '%':
            self._value = self._ch
            self._ch = mystr[self._p]

            if self._ch == '%':
                self._value += self._ch
                self._p += 1
                self._key = 'RESERVED'
                self._syn = 15      # '%%'
            elif self._ch == '/':
                self._value += self._ch
                self._p += 1
                self._ch = mystr[self._p]
                if self._ch == '%':
                    self._value += self._ch
                    self._p += 1
                    self._key = 'RESERVED'
                    self._syn =16      # '%/%'
            elif self._ch == 'i':
                self._value += self._ch
                self._p += 1
                self._ch = mystr[self._p]
                if self._ch == 'n':
                    self._value += self._ch
                    self._p += 1
                    self._ch = mystr[self._p]
                    if self._ch == '%':
                        self._value += self._ch
                        self._p += 1
                        self._key = 'RESERVED'
                        self._syn = 32    # '%in%'
            elif self._ch == '*':
                self._value += self._ch
                self._p += 1
                self._ch = mystr[self._p]
                if self._ch == '%':
                    self._value += self._ch
                    self._p += 1
                    self._key = 'RESERVED'
                    self._syn =33      # '%*%'

            else:
                self._syn = '@-6' #非法字符


        elif self._ch == '^':
            self._value = self._ch
            self._key = 'RESERVED'
            self._syn = 17     # '^'

        elif self._ch == '>':
            self._value = self._ch
            self._ch = mystr[self._p]

            if self._ch == '=':
                self._value += self._ch
                self._p += 1
                self._key = 'RESERVED'
                self._syn = 21     # '>='
            else:
                self._key = 'RESERVED'
                self._syn = 18     # '>'

        elif self._ch == '<':
            self._value = self._ch
            self._ch = mystr[self._p]

            if self._ch == '=':
                self._value += self._ch
                self._p += 1
                self._key = 'RESERVED'
                self._syn = 22     # '<='
            elif self._ch == '-':
                self._value += self._ch
                self._p += 1
                self._key = 'RESERVED'
                self._syn = 29     # '<-'
            elif self._ch == '<':
                self._value += self._ch
                self._p += 1
                self._ch = mystr[self._p]
                if self._ch == '-':
                    self._value += self._ch
                    self._p += 1
                    self._key = 'RESERVED'
                    self._syn = 29    # '<<-'
            else:
                self._key = 'RESERVED'
                self._syn = 19      # '<'

        elif self._ch == '=':
            self._value = self._ch
            self._ch = mystr[self._p]

            if self._ch == '=':
                self._value += self._ch
                self._p += 1
                self._key = 'RESERVED'
                self._syn = 20     # '=='
            else:
                self._key = 'RESERVED'
                self._syn = 29     # '='

        elif self._ch == '!':
            self._value = self._ch
            self._ch = mystr[self._p]

            if self._ch == '=':
                self._value += self._ch
                self._p += 1
                self._key = 'RESERVED'
                self._syn = 23      # '!='
            else:
                self._key = 'RESERVED'
                self._syn =  26     # '!'

        elif self._ch == '&':
            self._value = self._ch
            self._ch = mystr[self._p]

            if self._ch == '&':
                self._value += self._ch
                self._p += 1
                self._key = 'RESERVED'
                self._syn = 27      # '&&'
            else:
                self._key = 'RESERVED'
                self._syn = 24      # '&'

        elif self._ch == '|':
            self._value = self._ch
            self._ch = mystr[self._p]

            if self._ch == '|':
                self._value += self._ch
                self._p += 1
                self._key = 'RESERVED'
                self._syn = 28      # '||'
            else:
                self._key = 'RESERVED'
                self._syn = 25      # '|'

        elif self._ch == ':':
            self._value = self._ch
            self._key = 'RESERVED'
            self._syn = 31     # ':'



    def mergeElement(self):
        if self._tokens.__len__() != 0:
            if self._tokens[self._tokens.__len__() - 1][0] == '<-' and self._value == 'function':
                self._tokens.pop()
                self._value = '<-function'
                self._key = 'RESERVED'
                self._syn = 55

            if self._tokens[self._tokens.__len__() - 1][0] == '<-' and self._value == 'c':
                self._tokens.pop()
                self._value = '<-c'
                self._key = 'RESERVED'
                self._syn = 57



    def isBoolean(self):
        if self._syn == 43 or self._syn == 44:
            self._key = 'BOOLEAN'

    def getResult(self,mystr):
        while self._p != len(mystr):
            self.analysisCode(mystr)

            self.mergeElement()
            self.isBoolean()

            if self._syn != '':
                # print([self._value,self._key])
                #print([self._syn,self._value])
                self._tokens.append([self._value,self._key])
        # print(self._p)
        return self._tokens


