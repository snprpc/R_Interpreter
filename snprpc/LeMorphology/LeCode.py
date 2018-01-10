__author__ = '1'


class Code(object):
    # 保存所有代码
    __content = ''

    def readFile(self,address):

        myCode = open(address,'r')
        for line in myCode:
            if line != '\n':
                #截掉字符串左边的空格，去除空行
                line = line.lstrip()
                line = line.replace('\n',';\n')
                self.__content = "%s%s" %(self.__content,line.lstrip())

            else:
                self.__content = "%s%s" %(self.__content,line)
        # 为最后一行添加分号
        # self.__content = "%s%s" %(self.__content,';\n')
        myCode.close()
    # 去除注释
    def delAnnotation(self):
        state = 0
        index = -1
        temp = ''

        for i in self.__content:
            index += 1
            if state == 0:
                # 发现‘#’时，把状态改为1
                if i == '#':
                    state = 1
                    startIndex = index

            if state == 1:
                temp = temp + i
                #把确定为注释的一行替换为空，并把行数下标还原
                if i == '\n':
                    self.__content = self.__content.replace(temp,'')
                    state = 0
                    index = startIndex
                    temp = ''

    def getCode(self,address):
        self.readFile(address)
        self.delAnnotation()
        return self.__content
