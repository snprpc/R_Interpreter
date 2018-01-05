from snprpc.ast.LvExpression import LvExpression


class LvRightChild(LvExpression):
    __rChild = ''

    def getChild(self):
        return self.__rChild

    def setRightChild(self, rChild):
        self.__rChild = rChild