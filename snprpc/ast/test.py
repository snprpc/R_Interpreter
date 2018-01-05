from snprpc.ast.LvAddExpression import LvAddExpression
from snprpc.ast.LvLeftChild import LvLeftChild
from snprpc.ast.LvRightChild import LvRightChild

#leftchild = LvLeftChild()
#leftchild.setLeftChild('b')

leftchild = LvAddExpression()
llc = LvLeftChild()

llc.setLeftChild('1')
lrc = LvRightChild()
lrc.setRightChild('2')
leftchild.addLeftChild(llc)
leftchild.addRightChild(lrc)

rightchild = LvRightChild()
rightchild.setRightChild('a')

add = LvAddExpression()
add.addLeftChild(leftchild)
add.addRightChild(rightchild)

add.printTree()
