
from snprpc.ast.LvExpression import LvExpression


class LvAddExpression(LvExpression):
    __lChild = LvExpression()
    __rChild = LvExpression()

    def addLeftChild(self, lChild):
        self.__lChild = lChild

    def addRightChild(self, rChild):
        self.__rChild = rChild

    def getChile(self):
        self.getLeftChild()
        self.getRightChild()

    def getLeftChild(self):
        return self.__lChild

    def getRightChild(self):
        return self.__rChild

    def printTreeLeft(self):

        if self.getLeftChild().__class__.__name__ == "LvLeftChild":
            print(
                "|+" + self.getLeftChild().__class__.__name__ + ": " + self.getLeftChild().getChild() + '\n',
                end=''
            )
            return
        #print("|+" + self.getLeftChild().__class__.__name__ + '\n', end='')
        #self.getLeftChild().printTreeLeft()
        #self.getLeftChild().printRightChild()
        self.getLeftChild().printTree()

    def printTreeRight(self):
        if self.getRightChild().__class__.__name__ == "LvRightChild":
            print(
                "|+" + self.getRightChild().__class__.__name__ + " : " + self.getRightChild().getChild() + '\n',
                end=''
            )
            return
        #print("|+" + self.getLeftChild().__class__.__name__ + '\n', end='')
        #self.getRightChild().printTreeLeft()
        #self.getRightChild().printTreeRight()
        self.getRightChild().printTree()

    def printTree(self):
        print("|+" + self.getLeftChild().__class__.__name__ + '\n', end='')
        self.printTreeLeft()
        self.printTreeRight()

    def printRoot(self):
        self.getLeftChild()
        self.getRightChild()
