
from snprpc.ast.LvExpression import LvExpression


class LvLeftChild(LvExpression):
    __lChild = ''

    def getChild(self):
        return self.__lChild

    def setLeftChild(self, lChild):
        self.__lChild = lChild

