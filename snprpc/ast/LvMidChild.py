from snprpc.ast.LvExpression import LvExpression


class LvMidChild(LvExpression):
    __mChild = object

    def getChild(self):
        return self.__mChild

    def setLeftChild(self, mChild):
        self.__mChild = mChild