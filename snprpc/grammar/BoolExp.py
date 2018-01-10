from snprpc.grammar.Equality import Equality
from Leimport import *

class BoolExp(Equality):
    pass

class RelopBexp(BoolExp):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def __repr__(self):
        return 'RelopBexp(%s, %s, %s)' % (self.op, self.left, self.right)\

    def createAST(self, env):
        create1 = create()
        return create1.op(env, self.op, self.left.createAST(env), self.right.createAST(env))


# 与运算
class AndBexp(BoolExp):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return 'AndBexp(%s, %s)' % (self.left, self.right)

    def createAST(self, env):
        create1 = create()
        return create1.op(env, 'and', self.left.createAST(env), self.right.createAST(env))


# 或与算
class OrBexp(BoolExp):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return 'OrBexp(%s, %s)' % (self.left, self.right)

    def createAST(self, env):
        create1 = create()
        return create1.op(env, 'or', self.left.createAST(env), self.right.createAST(env))

# 非运算
class NotBexp(BoolExp):
    def __init__(self, exp):
        self.exp = exp

    def __repr__(self):
        return 'NotBexp(%s)' % self.exp

    def createAST(self, env):
        not1 = NOT(env)
        not1.setContent(self.exp.createAST(env))
        return not1